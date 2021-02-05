from flask.cli import AppGroup

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


@seed_commands.command('all')
def seed():
    pass


@seed_commands.command('undo')
def undo():
    pass
