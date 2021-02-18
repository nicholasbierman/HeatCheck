from app.models import db, Player
import requests
import json


def seed_players():
    players = json.loads(requests.get(
        'https://raw.githubusercontent.com/bttmly/nba/master/data/players.json').text)
    for player in players:
        if player['teamId'] == 0:
            caboclo = Player(
                first_name=player['firstName'],
                last_name=player["lastName"],
                team_id=1610612745,
                nba_player_id=player["playerId"]
            )
            db.session.add(caboclo)
            db.session.commit()
            db.session.flush()
        else:
            new_player = Player(
                first_name=player["firstName"],
                last_name=player["lastName"],
                team_id=player["teamId"],
                nba_player_id=player["playerId"]
            )
            db.session.add(new_player)
            db.session.commit()
            db.session.flush()


def undo_players():
    db.session.execute('TRUNCATE players CASCADE')
    db.session.commit()
