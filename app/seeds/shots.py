from app.models import db, Shot, Player
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
import json
import os


def scrape_shots_by_player_id(id):
    response = shotchartdetail.ShotChartDetail(
        team_id=0, player_id=id, season_nullable='2020-21',
        season_type_all_star='Regular Season', timeout=None
    )
    response_json = response.get_json()
    directory = 'app/player_shot_data'
    file = f"{id}.txt"
    if os.path.isdir(directory):
        path = os.path.join(directory, file)
        text_file = open(f"{path}", "w")
        text_file.write(f"{response_json}")
        text_file.close()
    else:
        directory = os.mkdir('app/player_shot_data')
        path = os.path.join(directory, file)
        text_file = open(f"{directory}/{id}.txt", "w")
        text_file.write(f"{response_json}")
        text_file.close()


def seed_shots():
    players = Player.query.all()
    for player in players:
        scrape_shots_by_player_id(player.nba_player_id)
        with open(f"app/player_shot_data/{player.nba_player_id}.txt") as file:
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


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
