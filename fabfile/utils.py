from __future__ import print_function
from sys import exit
import os

from fabric.colors import cyan
from fabric.api import *

from config import Keys, Remotes

class attr_dict(dict):
    def __getattr__(self, key):
        try:
            return(self[key])
        except KeyError:
            return(None)
    def __setattr__(self, key, value):
        self[key] = value

Cache = attr_dict()

def update_current():
    Cache.current_host = env.host
    env.user = Cache.users[env.host]
    env.key_filename = env.key_filename or \
            [os.path.expanduser(keyfile) for keyfile in Keys if os.path.exists(os.path.expanduser(keyfile))]
    Cache.deploy_env = Cache.envs[env.host]
    Cache.deploy_branch = Cache.branches[env.host]
    Cache.deploy_start = Cache.start[env.host]
    Cache.repo_path = Cache.paths[env.host]
    Cache.script_path = Cache.paths[env.host] + '/_misc/scripts'
    with hide('everything'):
        with settings(warn_only=True):
            with cd(Cache.script_path):
                out = run('./fabric_tasks.sh workon_name')
    Cache.workon = 'workon ' + out if out.succeeded else \
            'echo "unable to activate virtualenv"; exit 1'

def require_target(fn):
    def decorated(*args, **kwargs):
        if not env.host:
            print('run "fab on:<target> <command>" to specify target system.')
            exit()
        if env.host != Cache.current_host:
            if env.host not in Cache.paths:
                print('Unknown host: "{}"'.format(env.host))
                exit()
            update_current()
        fn(*args, **kwargs)

    decorated.__name__ = fn.__name__
    decorated.__doc__ = fn.__doc__
    return decorated

def populate_localhost():
    cwd = os.getcwd()
    Remotes['local']['user'] = os.environ['USER']
    Remotes['local']['path'] = cwd

def populate_cache(remotes):
    cwd = os.getcwd()
    if not os.path.exists(os.path.join(cwd,'.git')):
        print('ERROR: please run fab in repo root.')
        exit(1)
    Cache.local_repo = cwd
    with hide('everything'):
        working_branch = local('git symbolic-ref HEAD', capture=True)[11:]
    Cache.local_branch = working_branch
    if 'local' in remotes:
        populate_localhost()
    Cache.users = {}
    Cache.paths = {}
    Cache.envs = {}
    Cache.branches = {}
    Cache.start = {}
    for r in remotes:
        r = Remotes[r]
        if r['host'] in Cache.users.keys():
            print('fabric doesn\'t support deploying to different remotes with the same hostname.')
            exit(1)
        Cache.users[r['host']] = r['user']
        Cache.paths[r['host']] = r['path']
        Cache.envs[r['host']] = r['env']
        Cache.branches[r['host']] = r['branch']
        Cache.start[r['host']] = r['start']

