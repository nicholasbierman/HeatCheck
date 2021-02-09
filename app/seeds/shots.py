from app.models import db, Shot

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
