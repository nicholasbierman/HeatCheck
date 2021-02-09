from app.models import db, Player


def seed_players():
    curry = Player(
        nba_player_id=201939,
        first_name="Stephen",
        last_name="Curry",
        full_name="Stephen Curry"
    )
    harden = Player(nba_player_id=201935, first_name="James", last_name="Harden", full_name="James Harden")

    db.session.add(curry)
    db.session.add(harden)
    db.session.commit()


def undo_players():
    db.session.execute('TRUNCATE players CASCADE')
    db.session.commit()
