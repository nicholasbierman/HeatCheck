from flask import Blueprint, request
from nba_api.stats.endpoints import shotchartdetail
import json
import requests

shot_routes = Blueprint("shots", __name__)

teams = json.loads(requests.get(
    'https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json')
    .text)

players = json.loads(requests.get(
    'https://raw.githubusercontent.com/bttmly/nba/master/data/players.json')
    .text)


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


# @shot_routes.route('/<int:player_id>')
def get_shots_by_player_id(player_id):
    print("HITTING BACKEND ROUTE")
    shot_json = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=201939,
        context_measure_simple='PTS',
        season_nullable='2020-21',
        season_type_all_star='Regular Season')
    print(shot_json)
    # Load data into a Python dictionary
    shot_data = json.loads(shot_json.get_json())
    # Get the relevant data from our dictionary
    headers = shot_data['resultSets'][0]["headers"]
    data = shot_data['resultSets'][0]["rowSet"]
    shots = []
    for row in data:
        data_point = dict(zip(headers[16:19], row[16:19]))
        shots.append(data_point)
    return shots


print(get_shots_by_player_id(201939))
