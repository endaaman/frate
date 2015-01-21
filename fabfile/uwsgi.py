from fabric.api import task, local, run, put
import os

uwsgi_pid = 'tmp/uwsgi.pid'


def uwsgi_start():
    local('uwsgi uwsgi.yml')


def uwsgi_reload():
    local('uwsgi --reload %s' % uwsgi_pid)


def uwsgi_stop():
    local('kill -QUIT `cat %s`' % uwsgi_pid)


@task(default=True)
def uwsgi(param=None):
    started = os.path.exists('%s' % uwsgi_pid)
    stop = param == 'stop'
    if stop:
        if started:
            uwsgi_stop()
        else:
            print 'uwsgi process has not started.'
    else:
        if started:
            uwsgi_reload()
        else:
            uwsgi_start()


@task
def lookup():
    local('ps aux | grep uwsgi')
