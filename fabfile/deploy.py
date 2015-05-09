from fabric.api import task, run
# loda ssl env
try:
    from local import *
except:
    pass


@task(default=True)
def deploy():
    run('bash scripts/build.sh')
    
