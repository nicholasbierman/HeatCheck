from flask import Blueprint, request
from app.models import Shot
import json
import requests

shot_routes = Blueprint("shots", __name__)


def get_player_id(first, last):
    for player in players:
        if player['firstName'] == first and player['lastName'] == last:
            return player['playerId']
    return - 1


def get_team_id(team):
    for team in teams:
        if team['teamName'] == team:
            return team['teamId']
    return - 1


@shot_routes.route('/<int:player_id>')
def get_shots_by_player_id(player_id):
    shots = Shot.query.all()
    return {"shots": [shot.to_dict() for shot in shots]}
