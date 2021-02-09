from app.models import db, Shot
import requests
# base_request_url = "https://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2020-21&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=10&EndRange=28800&GameID=&GameSegment=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=201939&PlayerPosition=&RangeType=0&RookieYear=&Season=2020-21&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=1&StartRange=0&TeamID=0&VsConference=&VsDivision="
# headers_dict = {'origin': 'https://www.nba.com',
#                 'referer': 'https://www.nba.com/',
#                 'sec-fetch-dest': 'empty',
#                 'sec-fetch-node': 'cors',
#                 'sec-fetch-site': 'same-site',
#                 'x-nba-stats-origin': 'stats',
#                 'x-nba-stats-token': 'true',
#                 'Content-Type': 'application/json',
#                 'accept': 'text/html',
#                 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

# response = requests.get(base_request_url, headers=headers_dict)
# shots = response.json()['resultSets'][0]['rowSet']


def seed_shots():
    shot1 = Shot(nba_player_id=201939, x=100, y=100, shot_zone="Center")
    shot2 = Shot(nba_player_id=201939, x=250, y=150, shot_zone="Left Corner 3")
    shot3 = Shot(nba_player_id=201939, x=250, y=250)
    shot4 = Shot(nba_player_id=201939, x=0, y=0)
    shot5 = Shot(nba_player_id=201939, x=500, y=0)
    shot6 = Shot(nba_player_id=201939, x=0, y=470)
    shot7 = Shot(nba_player_id=201939, x=0, y=460)
    db.session.add(shot1)
    db.session.add(shot2)
    db.session.add(shot3)
    db.session.add(shot4)
    db.session.add(shot5)
    db.session.add(shot6)
    db.session.add(shot7)
    db.session.commit()


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
