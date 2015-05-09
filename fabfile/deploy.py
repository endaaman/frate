from fabric.api import task, run, cd

# load ssl env
try:
    from local import *
except:
    pass


@task(default=True)
def deploy():
    with cd('/var/www/frate'):
        run('bash scripts/build.sh')
