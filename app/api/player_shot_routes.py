from flask import Blueprint
from app.models.shot import db, Shot
import json
import requests

shot_routes = Blueprint("shots", __name__)


@shot_routes.route('/<int:id>')
def get_shots_by_player_id(id):
    shots = Shot.query.filter(Shot.nba_player_id == id)
    return {"shots": [shot.to_dict() for shot in shots]}


@shot_routes.route('/<int:id>/paint')
def get_shots_in_paint(id):
    paint_shots = Shot.query.filter(Shot.nba_player_id ==
                                    id and Shot.shot_zone == "paint")
    return {"paint_shots": [shot.to_dict() for shot in paint_shots]}


@shot_routes.route('/<int:id>/rightcorner3')
def get_right_corner_threes(id):
    shots = Shot.query.filter(
        Shot.nba_player_id == id)
    return {"right_corner_3s": [shot.to_dict() for shot in shots]}
