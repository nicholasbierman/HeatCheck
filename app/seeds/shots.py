from app.models import db, Shot
import requests
import json


def seed_shots():
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
    #     'PlayerID': id,
    #     'SeasonType': 'Regular Season',
    #     'TeamID': 0,
    #     'VsDivision': '',
    #     'VsConference': '',
    #     'SeasonSegment': '',
    #     'Season': '2018-19',
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
    # results = content["resultSets"][0]["rowSet"]
    # print(results[0])
    # for shot in results:
    #     new_shot = Shot(nba_player_id=shot[3], x=shot[17]+250, y=shot[18]+55,
    #                     shot_made_flag=shot[20], shot_zone=shot[14])
    #     db.session.add(new_shot)
    #     db.session.commit()
    #     db.session.flush()

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
             shot10, shot11, shot12, shot13, shot14, shot15}
    for shot in shots:
        db.session.add(shot)
        db.session.commit()
        db.session.flush()


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
