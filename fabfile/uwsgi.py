from fabric.api import task, local, run, put
import os

uwsgi_pid = 'tmp/uwsgi.pid'


def started():
    return os.path.exists('%s' % uwsgi_pid)


def do_start():
    local('uwsgi uwsgi.yml')


def do_reload():
    local('uwsgi --reload %s' % uwsgi_pid)


def do_stop():
    local('kill -QUIT `cat %s`' % uwsgi_pid)


@task(default=True)
def uwsgi(param=None):
    if started():
        do_reload()
    else:
        do_start()


@task
def stop():
    if started():
        do_stop()
    else:
        print('uwsgi process is not started')


@task
def start():
    if started():
        print('uwsgi process is already started')
    else:
        do_start()


@task
def reload():
    if started():
        do_reload()
    else:
        print('uwsgi process is not started')

@task
def lookup():
    local('ps aux | grep uwsgi')
