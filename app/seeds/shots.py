from app.models import db, Shot
from nba_api.stats.endpoints import shotchartdetail
import json
import requests


def seed_shots():
    shot = Shot(nba_player_id=201939, x=100, y=100, shot_zone="Center")
    db.session.add(shot)
    db.session.commit()


def undo_shots():
    db.session.execute('TRUNCATE shots')
    db.session.commit()
