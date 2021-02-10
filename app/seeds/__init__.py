from flask.cli import AppGroup
from .players import seed_players, undo_players
from .shots import seed_shots, undo_shots
from .league_averages import seed_league_averages, undo_league_averages

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the 'flask seed all' command
@seed_commands.command('all')
def seed():
    seed_players()
    seed_shots()
    seed_league_averages()

# Creates the 'flask seed undo' command
@seed_commands.command('undo')
def undo():
    undo_players()
    undo_shots()
    undo_league_averages()
