# -*- coding: utf-8 -*-

Roles = {
        'prod': ['aws', 'rack0'],
        'qa': ['dev'],
        }

Remotes = {
        'aws': {
            'host': "development.tukeq.com",
            'port': "22",
            'user': "ubuntu",
            'path': "~/projects/tukeq-atlantis",
            'env': "prod",
            'branch': 'live',
            'start': 'toureet-web',
            },
        'rack0': {
            'host': "rack0.tukeq.com",
            'port': "2221",
            'user': "dev",
            'path': "~/development/tukeq-atlantis",
            'env': "prod",
            'branch': 'live',
            'start': 'toureet-web',
            #'start': 'tornado:*',
            },
        'dev': {
            'host': "dev.tukeq.com",
            'port': "22",
            'user': "dev",
            'path': "~/development/tukeq-atlantis",
            'env': "qa",
            'branch': 'master',
            'start': 'toureet-web',
            #'start': 'tornado:*',
            },
        'local': {
            'host': "localhost",
            'port': "22",
            'user': "nobody", #$USER
            'path': "/dev/null", #$PWD
            'env': "dev",
            'branch': 'master',
            'start': '',
            },
        }

Keys = ['~/.ssh/id_rsa.d/tukeq-rack0', '~/.ssh/id_rsa.d/tukeq-admin']

AptDependencies = "python-pip python-dev git mongodb redis-server libgraphicsmagick++1-dev libboost-python-dev csstidy rabbitmq-server nginx supervisor rsync node-less node-uglify"
