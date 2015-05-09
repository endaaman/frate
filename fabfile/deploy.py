from fabric.api import run

# loda ssl env
try:
    from local import *
except:
    pass


@task(default=True)
def deploy():
    run('scripts/build.sh')
