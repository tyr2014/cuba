from fabric.api import *
from fabric.colors import *

from utils import require_target

@task
@require_target
def supervisord(arg='status'):
    with settings(warn_only=True):
        sudo('/etc/init.d/supervisor ' + arg)

@task
@require_target
def nginx(arg='status'):
    with settings(warn_only=True):
        sudo('/etc/init.d/nginx ' + arg)

@task
@require_target
def mongodb(arg='status'):
    with settings(warn_only=True):
        sudo('/etc/init.d/mongodb ' + arg)

@task
@require_target
def redis(arg='status'):
    with settings(warn_only=True):
        sudo('/etc/init.d/redis-server ' + arg)

@task
@require_target
def rabbitmq(arg='status'):
    with settings(warn_only=True):
        sudo('/etc/init.d/rabbitmq-server ' + arg)

@task
@require_target
def supervisorctl(arg='status'):
    with settings(warn_only=True):
        with hide('everything'):
            out = run('supervisorctl pid')
    if out.failed:
        print(yellow('WARN') + ' - supervisord is not running. [aborting]')
        exit(1)
    run('supervisorctl ' + arg)

@task
def list():
    msg = '''\
    running services:
        supervisord
        nginx
        mongodb
        redis
        rabbitmq
        --
        supervisorctl
    supervisor groups:
        tornado
        celery
    '''
    print(msg)

@task(default=True)
@require_target
def all(arg='status'):
    execute(supervisord, arg)
    execute(nginx, arg)
    execute(mongodb, arg)
    execute(redis, arg)
    execute(rabbitmq, arg)

