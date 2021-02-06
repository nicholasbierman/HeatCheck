from flask.cli import AppGroup
from .players import seed_players, undo_players
from .shots import seed_shots, undo_shots

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the 'flask seed all' command
@seed_commands.command('all')
def seed():
    seed_players()
    seed_shots()

# Creates the 'flask seed undo' command
@seed_commands.command('undo')
def undo():
    undo_players()
    undo_shots()
