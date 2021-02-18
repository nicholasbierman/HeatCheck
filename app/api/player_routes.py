from flask import Blueprint, request
from app.models.player import Player

player_routes = Blueprint('player', __name__)


@player_routes.route('/<int:id>')
def get_player_by_id(id):
    player = Player.query.filter_by(nba_player_id=id).first()
    return player.to_dict()
