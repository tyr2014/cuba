import os
from datetime import datetime

from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm

from utils import require_target, Cache

def repo_status():
    retval = {"clean": True, "errmsg": '', }
    with hide('everything'):
        with cd(Cache.repo_path):
            # strips 'refs/heads/'
            retval['branch'] = run('git symbolic-ref HEAD')[11:]
            if retval['branch'] != Cache.deploy_branch:
                retval['clean'] = False
                retval['errmsg'] += 'remote branch is "' + retval['branch'] + '".\n'
            retval['status'] = run('git status')
            retval['status-s'] = run('git status -s')
            if retval['status-s'] != '':
                retval['clean'] = False
                retval['errmsg'] += 'uncommitted changes found:\n' + retval['status-s']
    return retval

@task
@require_target
def hard_reset():
    status = repo_status()
    if not status['clean']:
        print(yellow('WARN') + ' - ' + status['errmsg'])
        ans = confirm('reset --hard anyway?', default=False)
        if not ans:
            exit(1)
    with cd(Cache.repo_path):
        run('git reset --hard')

@task
@require_target
def pull_changes():
    status = repo_status()
    if not status['clean']:
        print(yellow('ERROR') + ' - ' + status['errmsg'])
        #ans = confirm('pull changes anyway?', default=False)
        #if not ans:
        #    exit(1)
        exit(1)
    with cd(Cache.repo_path):
        run('git fetch')
        run('git reset --hard origin/' + Cache.deploy_branch)

@task
@require_target
def synccompress(noforce=''):
    param = '' if noforce == 'noforce' else ' --force'
    execute(manage, 'synccompress' + param)

@task
@require_target
def nginx():
    local_dir = '{}/_misc/skeleton/{}/nginx/'.format(Cache.local_repo, 
            env.host)
    if not os.path.isdir(local_dir):
        print('Nginx conf files for host "' + green(env.host, True) + \
                '" is not present. [Aborting]')
        exit(1)
    with hide('everything'):
        tmp_dir = run('mktemp -d') + '/'
    remote_dir = env.user + '@' + env.host + ':' + tmp_dir
    local('rsync -rtz {} {}'.format(local_dir, remote_dir))
    conf_dir = '/etc/nginx'
    backup_dir = '/var/backups/nginx.' + \
            datetime.now().strftime('%Y%m%d%H%M%S') + '/'
    sudo('rsync -brt --backup-dir {} {} {}'.format(backup_dir, 
        tmp_dir, conf_dir))
    init_script = '/etc/init.d/nginx '
    with settings(warn_only=True):
        with hide('warnings'):
            out = sudo(init_script + 'reload')
    if out.failed:
        print(red('ERROR', True) + \
                ': invalid nginx conf files used. reverting changes.')
        sudo('rsync -rt {} {}'.format(backup_dir, conf_dir))
    with hide('everything'):
        run('rm -r ' + tmp_dir)

@task
@require_target
def supervisord():
    local_file = '{}/_misc/skeleton/{}/supervisor/supervisord.conf'.format(Cache.local_repo, env.host)
    if not os.path.isfile(local_file):
        print('supervisord.conf for host "' + green(env.host, True) + \
                '" is not present. [Aborting]')
        exit(1)
    with hide('everything'):
        tmp_file = local('mktemp', capture=True)
    local('cp -p {} {}'.format(local_file, tmp_file))
    remote_file = env.user + '@' + env.host + ':' + tmp_file
    local('rsync -tz {} {}'.format(tmp_file, remote_file))
    with hide('everything'):
        local('rm -r ' + tmp_file)
    conf_dir = '/etc/supervisor'
    conf_file = conf_dir + '/supervisord.conf'
    backup_dir = '/var/backups/supervisor.' + \
            datetime.now().strftime('%Y%m%d%H%M%S') + '/'
    sudo('rsync -bt --backup-dir {} {} {}'.format(backup_dir, 
        tmp_file, conf_file))
    init_script = '/etc/init.d/supervisor '
    with settings(warn_only=True):
        with hide('warnings'):
            out = sudo(init_script + 'restart')
    if out.failed:
        print(red('ERROR', True) + \
                ': invalid supervisord.conf used. reverting changes.')
        sudo('rsync -rt {} {}'.format(backup_dir, conf_dir))
    with hide('everything'):
        run('rm -r ' + tmp_file)

@task
@require_target
def git_status():
    with cd(Cache.repo_path):
        run('git status')

@task
@require_target
def switch_branch(quiet=''):
    quiet = (quiet == 'quiet' or quiet == 'q')
    status = repo_status()
    if status['branch'] == Cache.deploy_branch:
        print('remote is already on branch "' + Cache.deploy_branch + '". [skipping]')
        return
    if not status['clean'] and not quiet:
        print(yellow('WARN') + ' - ' + status['errmsg'])
        ans = confirm('switching anyway?', default=False)
        if not ans:
            exit(1)
    with cd(Cache.repo_path):
        run('git fetch origin')
        run('git branch --track -f {} origin/{}'.format(Cache.deploy_branch, Cache.deploy_branch))
        run('git checkout ' + Cache.deploy_branch)

@task
@require_target
def clear_cache(index=''):
    if not index:
        ans = confirm('You\'re trying to clear '+ red('ALL', True) + \
                ' cached data!?', default=False)
        if not ans:
            exit(1)
    execute(manage, 'clear_cache ' + index)

@task
@require_target
def manage(command=''):
    if not command:
        print('argument required')
        exit(1)
    with prefix(Cache.workon):
        if Cache.deploy_env in ['prod','qa']:
            with hide('everything'):
                sudo('chmod -R g+w ./log')
        run('./manage.py ' + command)

@task
@require_target
def run_once():
    with cd(Cache.script_path):
        run('./fabric_tasks.sh run_once')

def deploy_local():
    execute("install.apt_dependencies")
    execute("install.pip_dependencies")
    execute("install.npm_dependencies")
    execute("install.apply_patches")
    execute(run_once)

def deploy_remote(tasks):
    full = (tasks != 'fast')
    ans = confirm('Deploy to remote: ' + green(env.host, True))
    if not ans:
        return
    if Cache.deploy_env not in ['prod','qa']:
        print('unsupported deploy_env: ' + green(Cache.deploy_env, True))
        exit(1)
    if Cache.deploy_branch != Cache.local_branch:
        ans = confirm('remote is configured to use branch "' + green(Cache.deploy_branch) +
                '", use current working branch "' + green(Cache.local_branch) + '" instead?', default=False)
        if ans:
            Cache.deploy_branch = Cache.local_branch
    switch_branch('quiet')
    if full:
        execute(hard_reset)
    execute(pull_changes)
    if full:
        execute("install.apt_dependencies")
        execute("install.pip_dependencies")
        execute("install.npm_dependencies")
        execute("install.apply_patches")
        execute(run_once)
        execute(clear_cache)
    execute(synccompress)
    if Cache.deploy_start:
        execute("service.supervisorctl", "restart " + Cache.deploy_start)
    print('deployment completed successfully.')

@task
def list():
    msg = '''\
    # on remote host
    fast deploy:
        pull_changes
        synccompress
        service.supervisorctl:"restart <remote.start>"
    full deploy:
        # deploy:full
        hard_reset
        pull_changes
        install.apt_dependencies
        install.pip_dependencies
        install.npm_dependencies
        install.apply_patches
        run_once
        clear_cache
        synccompress
        service.supervisorctl:"restart <remote.start>"
    # on localhost
        install.apt_dependencies
        install.pip_dependencies
        install.npm_dependencies
        install.apply_patches
        run_once
    remote config files:
        nginx
        supervisord
    other jobs:
        git_status
        switch_branch
    '''
    print(msg)

@task(default=True)
@require_target
def deploy_full(tasks='fast'):
    if env.host == 'localhost':
        execute(deploy_local)
    else:
        execute(deploy_remote, tasks)

