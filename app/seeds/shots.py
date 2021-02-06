from app.models import db, Shot
from nba_api.stats.endpoints import shotchartdetail
import json
import requests


def seed_shots():
    shot_json = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=201939,
        context_measure_simple='PTS',
        season_nullable='2020-21',
        season_type_all_star='Regular Season')
    shot_data = json.loads(shot_json.get_json())
    headers = shot_data['resultSets'][0]["headers"]
    data = shot_data['resultSets'][0]["rowSet"]
    for row in data:
        row = Shot(nba_player_id=201939,
                    x=data[17], y=data[18], shot_zone_range=data[15])
        db.session.add(row)
    db.session.commit()


def undo_shots():
    db.session.execute('TRUNCATE shots')
    db.session.commit()
