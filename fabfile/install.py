from sys import exit

from fabric.colors import green
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
from fabric.api import cd, env, execute, hide, local, run, settings, sudo, task

from config import AptDependencies, Keys
from utils import require_target, Cache

@task
@require_target
def sync_pip_cache():
    ans = confirm('Sync pip packages with remote host?', default=False)
    if not ans:
        return
    cache_dir = '~/.cache/pip/'
    cache_dir_rel = '.cache/pip/'
    remote_dir = env.user + '@' + env.host + ':' + cache_dir_rel
    with hide('everything'):
        local('mkdir -p ' + cache_dir)
        run('mkdir -p ' + cache_dir)
    local('rsync -hprtuvz {} {}'.format(cache_dir, remote_dir))
    local('rsync -hprtuvz {} {}'.format(remote_dir, cache_dir))

@task
def local_pip_cache():
    ans = confirm('Sync pip packages with local cache?', default=False)
    if not ans:
        return
    remote_dir = 'dev@dev.tukeq.com:.cache/pip/'
    local_dir = '~/.cache/pip/'
    with hide('everything'):
        local('mkdir -p ' + local_dir)
    local('rsync -hprtuvz {} {}'.format(remote_dir, local_dir))
    local('rsync -hprtuvz {} {}'.format(local_dir, remote_dir))

@task
@require_target
def apt_dependencies():
    if env.host == 'localhost':
        ans = confirm('use aptitude to update local dependent packages?', default=False)
        if not ans:
            return
    sudo('aptitude install -R -y ' + AptDependencies)

@task
@require_target
def checkout_code():
    if exists(Cache.repo_path + '/.git'):
        print('repo exists on remote host.')
        execute("deploy.switch_branch")
        execute("deploy.pull_changes")
        return
    with settings(warn_only=True):
        with hide('warnings'):
            out = run('ssh git@github.com -T 2>&1 | grep -q "successfully authenticated"')
    if out.failed:
        key_file = Keys[0]
        remote_file = env.user + '@' + env.host + ':' + key_file
        local('rsync {} {}'.format(key_file, remote_file))
        run('chmod 0400 ' + key_file)
    github = 'git@github.com:tyrchen/atlantis.git'
    run('git clone ' + github + ' ' + Cache.repo_path)
    execute("deploy.switch_branch")

@task
@require_target
def set_deploy_env():
    print('setting deploy_env for remote host: ' + green(Cache.deploy_env, True))
    with cd(Cache.script_path):
        run('./fabric_tasks.sh set_deploy_env ' + Cache.deploy_env)

@task
@require_target
def bashrc():
    with cd(Cache.script_path):
        run('./fabric_tasks.sh install_bashrc')
    with settings(warn_only=True):
        with hide('everything'):
            out = run('hash workon')
    if out.failed:
        print('ERROR: "workon" is not sourced.')
        exit(1)

@task
@require_target
def virtualenv():
    with hide('everything'):
        with settings(warn_only=True):
            out = run('hash virtualenv')
    if out.failed:
        print('"virtualenv" is not found. installing it with pip.')
        sudo('pip install --download-cache=~/.cache/pip virtualenv')
    execute(bashrc)
    with cd(Cache.script_path):
        run('./fabric_tasks.sh mkvirtualenv')

@task
@require_target
def pip_dependencies():
    if env.host == 'localhost':
        execute(local_pip_cache)
    else:
        execute(sync_pip_cache)
    with cd(Cache.script_path):
        run('./fabric_tasks.sh install_pip_deps')

@task
@require_target
def npm_dependencies():
    with cd(Cache.script_path):
        run('./fabric_tasks.sh check_npm_deps')

@task
@require_target
def apply_patches():
    ans = confirm('Apply patches?', default=False)
    if not ans:
        return
    with cd(Cache.script_path):
        run('./fabric_tasks.sh apply_patches')

@task
@require_target
def supervisor_init_script():
    init_file = '/etc/init.d/supervisor'
    sudo(init_file + ' stop')
    local_file = '{}/_misc/skeleton/supervisor_init_script.sh'.format(Cache.local_repo)
    with hide('everything'):
        tmp_file = local('mktemp', capture=True)
    local('cp -p {} {}'.format(local_file, tmp_file))
    remote_file = env.user + '@' + env.host + ':' + tmp_file
    local('rsync -tz {} {}'.format(tmp_file, remote_file))
    with hide('everything'):
        local('rm -r ' + tmp_file)
    sudo('mv {} {}'.format(tmp_file, init_file))
    sudo('chmod +x ' + init_file)
    sudo(init_file + ' start')

def install_local():
    execute(set_deploy_env)
    execute(virtualenv)
    execute(pip_dependencies)
    execute(npm_dependencies)
    execute(apply_patches)
    execute("deploy.run_once")
    print('Installation finished. Make sure mongod and redis-server are up and running.\n\nCall ". ~/.bashrc", then "workon" into the virtualenv and run "./manage.py runserver" to start the local webserver.')

def install_remote():
    ans = confirm('Run all install tasks on remote: ' + \
            green(env.host, True))
    if not ans:
        return
    if Cache.deploy_env not in ['prod','qa']:
        print('unsupported deploy_env: ' + green(Cache.deploy_env, True))
        exit(1)
    execute(apt_dependencies)
    execute(checkout_code)
    execute(set_deploy_env)
    execute(virtualenv)
    execute(pip_dependencies)
    execute(npm_dependencies)
    execute(apply_patches)
    execute("deploy.run_once")
    execute("deploy.synccompress")
    execute("deploy.nginx")
    execute(supervisor_init_script)
    execute("deploy.supervisord")
    print('Installation finished. check if production server is up.')

@task
def list():
    msg = '''\
    full install:
        apt_dependencies
        checkout_code
        set_deploy_env
        virtualenv
        pip_dependencies
        npm_dependencies
        apply_patches
        deploy.run_once
        deploy.synccompress
        deploy.nginx
        supervisor_init_script
        deploy.supervisord
        --
        (on:local)
    other jobs:
        sync_pip_cache
        local_pip_cache
        bashrc
    '''
    print(msg)

@task(default=True)
@require_target
def install_full():
    if env.host == 'localhost':
        execute(install_local)
    else:
        execute(install_remote)

