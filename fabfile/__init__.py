# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import exit

from fabric.api import *
from fabric.colors import cyan, green

from config import *
from utils import populate_cache, require_target, Cache
import service
import install
import deploy

@task(default=True)
def usage(format='short'):
    print('SYNOPSIS:')
    print(cyan('\tfab usage:1'))
    print(cyan('\tfab on:<remote|group> <task>[:arg] | raw:<command>'))
    print(cyan('\tfab roles[:<role>] | remotes[:<remote>]'))
    print(cyan('\tfab --list | --help'))
    if format == 'short':
        return
    print('\npredefined tasks include:\n')
    print('[install]')
    execute(install.list)
    print('[deploy]')
    execute(deploy.list)
    print('[service]')
    execute(service.list)

@task
def roles(role=None):
    if not role or role not in Roles:
        print("SYNOPSIS: fab roles:<role>")
        print("available roles are: ", end='')
        print(green([r for r in iter(Roles)]))
    else:
        print(Roles[role])

    exit()

@task
def remotes(remote=None):
    if not remote or remote not in Remotes:
        print("SYNOPSIS: fab remotes:<remote>")
        print("available remotes are: ", end='')
        print(green([r for r in iter(Remotes)]))
    else:
        print(Remotes[remote])

    exit()

@task
def on(target=None):
    if target in Remotes:
        env.hosts = [Remotes[target]['host'] + ":" + Remotes[target]['port']]
        remotes = [target]
    elif target in Roles:
        env.hosts = [Remotes[r]['host'] + ":" + Remotes[r]['port'] for r in Roles[target]]
        remotes = [r for r in Roles[target]]
    else:
        print('SYNOPSIS: ' + cyan('on:<target>'))
        print("specify target system to run task on.")
        print("target can be a role or a remote.")
        print("available roles are: ", end='')
        print(green([r for r in iter(Roles)], True))
        print("available remotes are: ", end='')
        print(green([r for r in iter(Remotes)], True))
        print('run "fab roles/remotes" to show target details.')
        exit()

    populate_cache(remotes)

@task
@require_target
def raw(cmd_string=None):
    if not cmd_string:
        print('please provide the raw command you wanna run on the remote host as a string argument.')
        return
    with prefix(Cache.workon):
        run(cmd_string)

