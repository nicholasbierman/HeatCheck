from flask import Blueprint, request
from app.models.player import Player

player_routes = Blueprint('player', __name__)

@player_routes.route('/<int:id>')
def get_player_by_id(id):
    player = Player.query.filter(Player.nba_player_id == id)
    return player.to_dict()
