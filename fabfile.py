from fabric.api import env, roles, run, cd

# Define sets of servers as roles
env.roledefs = {
    'web': ['theguestandthehost.com'],
}

# Set the user to use for ssh
env.user = 'ericclients'
     
@roles('web')
def deploy():
    with cd('~/theguestandthehost.com/'):
        run('git pull')

