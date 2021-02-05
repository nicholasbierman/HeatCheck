from app.models import db, Player


def seed_players():
    curry = Player(
        nba_player_id=201939,
        first_name="Stephen",
        last_name="Curry",
        full_name="Stephen Curry"
    )

    db.session.add(curry)
    db.session.commit()


def undo_players():
    db.session.execute('TRUNCATE players')
    db.session.commit()
