from nba_api.stats.endpoints import shotchartdetail
import json
import requests

teams = json.loads(requests.get(
    'https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json').text)

players = json.loads(requests.get(
    'https://raw.githubusercontent.com/bttmly/nba/master/data/players.json').text)


def get_team_id(team):
    for team in teams:
        if team['teamName'] == team:
            return team['teamId']
    return - 1


def get_player_id(first, last):
    for player in players:
        if player['firstName'] == first and player['lastName'] == last:
            return player['playerId']
    return - 1


shot_json = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=get_player_id("Stephen", "Curry"),
    context_measure_simple='PTS',
    season_nullable='2020-21',
    season_type_all_star='Regular Season')

# Load data into a Python dictionary
shot_data = json.loads(shot_json.get_json())


# Get the relevant data from our dictionary
headers = shot_data['resultSets'][0]["headers"]
data = shot_data['resultSets'][0]["rowSet"]
for row in data:
    data_point = dict(zip(headers[16:19], row[16:19]))
    print(shot)
