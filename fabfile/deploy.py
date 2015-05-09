from fabric.api import task, run, prefix, cd

# loda ssl env
try:
    from local import *
except:
    pass


@task(default=True)
def deploy():
    run("source ~/.bash_profile")
    with cd('/var/www/frate'), prefix('workon frate'):
        run('git pull origin master')
        run('pip install -r freeze.txt')
        run('bower install')
        run('python manage.py migrate')
        run('python manage.py collectstatic')
        run('fab uwsgi')
