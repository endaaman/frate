from fabric.api import task, local, run, prefix, cd

# loda ssl env
try:
    from local import *
except:
    pass


@task(default=True)
def t():
    with cd('/var/www/frate'), prefix('workon frate'):
        run('git pull origin master')
        run('pip install -r freeze.txt')
        run('python manage.py migrate')
        run('python manage.py collectstatic')
        run('fab uwsgi')
