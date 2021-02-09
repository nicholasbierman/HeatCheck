from flask import Blueprint, request
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
    base_request_url = "https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=2020-21&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=201935&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2020-21&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID="
    headers_dict = {'origin': 'https://www.nba.com',
                    'referer': 'https://www.nba.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-node': 'cors',
                    'sec-fetch-site': 'same-site',
                    'x-nba-stats-origin': 'stats',
                    'x-nba-stats-token': 'true',
                    'Content-Type': 'application/json',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

    response = requests.get(base_request_url, headers=headers_dict)
    shots = response.json()['resultSets'][0]['rowSet']
    return {"shots": list(shots)}
