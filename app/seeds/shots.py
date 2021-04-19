from app.models import db, Shot, Player
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
import json


def scrape_shots_by_player_id(id):
    response = shotchartdetail.ShotChartDetail(
        team_id=0, player_id=id, season_nullable='2020-21',
        season_type_all_star='Regular Season', timeout=None
    )
    response_json = response.get_json()
    data = json.loads(response_json)
    shot_list = data["resultSets"][0]["rowSet"]
    for shot in shot_list:
        new_shot = Shot(nba_player_id=shot[3],
                        x=shot[17]+250,
                        y=shot[18]+60,
                        shot_zone=f'{shot[13]} - {shot[14]}',
                        shot_made_flag=shot[20])
        db.session.add(new_shot)
        db.session.commit()
        db.session.flush()


def seed_shots():
    # players = Player.query.all()
    # for player in players:
    #     scrape_shots_by_player_id(player.nba_player_id)
    with open('app/seeds/curry_shot_data.txt') as file:
        data = json.load(file)
        shot_list = data["resultSets"][0]["rowSet"]
        for shot in shot_list:
            new_shot = Shot(nba_player_id=shot[3],
                            x=shot[17]+250,
                            y=shot[18]+60,
                            shot_zone=f'{shot[13]} - {shot[14]}',
                            shot_made_flag=shot[20])
            db.session.add(new_shot)
            db.session.commit()
            db.session.flush()

    with open('app/seeds/harden_shot_data.txt') as file:
        data = json.load(file)
        shot_list = data["resultSets"][0]["rowSet"]
        for shot in shot_list:
            new_shot = Shot(nba_player_id=shot[3], x=shot[17]+250,
                            y=shot[18]+60,
                            shot_zone=f'{shot[13]} - {shot[14]}',
                            shot_made_flag=shot[20])
            db.session.add(new_shot)
            db.session.commit()
            db.session.flush()

    with open('app/seeds/zion_shot_data.txt') as file:
        data = json.load(file)
        shot_list = data["resultSets"][0]["rowSet"]
        for shot in shot_list:
            new_shot = Shot(nba_player_id=shot[3], x=shot[17]+250,
                            y=shot[18]+60,
                            shot_zone=f'{shot[13]} - {shot[14]}',
                            shot_made_flag=shot[20])
            db.session.add(new_shot)
            db.session.commit()
            db.session.flush()


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
