from app.models import db, Shot


def seed_shots():
    shot1 = Shot(nba_player_id=201939, x=100, y=100, shot_zone="Center")
    shot2 = Shot(nba_player_id=201939, x=250, y=150, shot_zone="Left Corner 3")
    db.session.add(shot1)
    db.session.add(shot2)
    db.session.commit()


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
