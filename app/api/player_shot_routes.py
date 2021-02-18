from flask import Blueprint, request
from app.models.shot import Shot
import json
import requests

shot_routes = Blueprint("shots", __name__)


@shot_routes.route('/<int:id>')
def get_shots_by_player_id(id):
    shots = Shot.query.filter(Shot.nba_player_id == id)
    return {"shots": [shot.to_dict() for shot in shots]}


# url_base = 'https://stats.nba.com/stats/shotchartdetail'

# headers = {
#     'Host': 'stats.nba.com',
#     'Connection': 'keep-alive',
#     'Accept': 'application/json, text/plain, */*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
#     'Referer': 'https://stats.nba.com/',
#     "x-nba-stats-origin": "stats",
#     "x-nba-stats-token": "true",
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9',
# }

# parameters = {
#     'ContextMeasure': 'PTS',
#     'LastNGames': 0,
#     'LeagueID': '00',
#     'Month': 0,
#     'OpponentTeamID': 0,
#     'Period': 0,
#     'PlayerID': 201935,
#     'SeasonType': 'Regular Season',
#     'TeamID': 0,
#     'VsDivision': '',
#     'VsConference': '',
#     'SeasonSegment': '',
#     'Season': '2020-2021',
#     'RookieYear': '',
#     'PlayerPosition': '',
#     'Outcome': '',
#     'Location': '',
#     'GameSegment': '',
#     'GameId': '',
#     'DateTo': '',
#     'DateFrom': ''
# }


# response = requests.get(url_base, params=parameters, headers=headers)
# content = json.loads(response.content)
# result_sets = content["resultSets"][0]["rowSet"][0][0]
