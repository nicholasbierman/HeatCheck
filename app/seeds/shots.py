from app.models import db, Shot
import requests
# base_request_url = "https://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2020-21&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=10&EndRange=28800&GameID=&GameSegment=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=201939&PlayerPosition=&RangeType=0&RookieYear=&Season=2020-21&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=1&StartRange=0&TeamID=0&VsConference=&VsDivision="
# headers_dict = {'origin': 'https://www.nba.com',
#                 'referer': 'https://www.nba.com/',
#                 'sec-fetch-dest': 'empty',
#                 'sec-fetch-node': 'cors',
#                 'sec-fetch-site': 'same-site',
#                 'x-nba-stats-origin': 'stats',
#                 'x-nba-stats-token': '1',
#                 'Content-Type': 'application/json',
#                 'accept': 'text/html',
#                 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

# response = requests.get(base_request_url, headers=headers_dict)
# shots = response.json()['resultSets'][0]['rowSet']


def seed_shots():
    shot3 = Shot(nba_player_id=201939, x=250, y=250,
                 shot_zone="Restriced Area - Center(C)", shot_made_flag=1)
    shot1 = Shot(nba_player_id=201939, x=200, y=250,
                 shot_zone="In The Paint(Non-RA) - Left Side(L)",
                 shot_made_flag=1)
    shot2 = Shot(nba_player_id=201939, x=250, y=350,
                 shot_zone="In The Paint(Non-RA) - Center(C)",
                 shot_made_flag=1)
    shot4 = Shot(nba_player_id=201939, x=300, y=250,
                 shot_zone="In The Paint(Non-RA) - Right Side(L)",
                 shot_made_flag=1)
    shot4 = Shot(nba_player_id=201939, x=470, y=0,
                 shot_zone="Right Corner 3 - Right Side(R)",
                 shot_made_flag=1)
    shot5 = Shot(nba_player_id=201939, x=10, y=0,
                 shot_zone="Left Corner 3 - Left Side(L)", shot_made_flag=1)
    shot7 = Shot(nba_player_id=201939, x=250, y=250,
                 shot_zone="Back Court - Backcourt(BC)", shot_made_flag=1)
    shot8 = Shot(nba_player_id=201939, x=300, y=170, shot_made_flag=0,
                 shot_zone="Mid-Range - Right Side(R)")
    shot9 = Shot(nba_player_id=201939, x=50, y=170,
                 shot_zone="Mid-Range - Left Side(R)", shot_made_flag=0)
    shot10 = Shot(nba_player_id=201939, x=250, y=170,
                  shot_zone="Mid-Range - Center(C)", shot_made_flag=0)
    shot11 = Shot(nba_player_id=201939, x=220, y=170,
                  shot_zone="Mid-Range - Left Center(LC)",
                  shot_made_flag=0)
    shot12 = Shot(nba_player_id=201939, x=280, y=170,
                  shot_zone="Mid-Range - Right Center(RC)",
                  shot_made_flag=0)
    shot13 = Shot(nba_player_id=201939, x=250, y=250,
                  shot_zone="Above the Break 3 - Center(C)",
                  shot_made_flag=0)
    shot14 = Shot(nba_player_id=201939, x=300, y=260,
                  shot_zone="Above the Break 3 - Right Center(RC)",
                  shot_made_flag=0)
    shot15 = Shot(nba_player_id=201939, x=220, y=250,
                  shot_zone="Above the Break 3 - Left Center(LC)")
    shots = {shot1, shot2, shot3, shot4, shot5, shot7, shot8,
             shot9, shot10, shot11, shot12, shot13, shot14, shot15}
    for shot in shots:
        db.session.add(shot)
        db.session.commit()
        db.session.flush()


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
