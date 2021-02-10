from flask import Blueprint, request
from app.models import Shot
import json
import requests

shot_routes = Blueprint("shots", __name__)


@shot_routes.route('/<int:id>')
def get_shots_by_player_id(id):
    shots = Shot.query.filter(Shot.nba_player_id == id)
    return {"shots": [shot.to_dict() for shot in shots]}
