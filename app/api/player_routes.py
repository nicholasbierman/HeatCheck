from flask import Blueprint, request
from app.models.player import Player

player_routes = Blueprint('player', __name__)


@player_routes.route('/<int:id>')
def get_player_by_id(id):
    # Have to use .first() here
    # To get Player object instead of BaseQuery object
    player = Player.query.filter_by(nba_player_id=id).first()
    return player.to_dict()


@player_routes.route('/all')
def get_all_players():
    players = Player.query.all()
    print(players)
    return {"allPlayers": [player.to_dict() for player in players]}
