from fabric.api import task, local, run, prefix, env, cd

env.hosts = '133.242.149.25'
env.port = 4545
env.user = 'endaken'
env.password = 'hoge'
env.key_filename = '~/.ssh/sakura'

@task(default=True)
def t():
    with cd('~/sites/frate'):
        run('git pull origin master')
