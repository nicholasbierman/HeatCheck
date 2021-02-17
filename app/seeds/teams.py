from app.models import db, Team
import requests
import json

def seed_teams():
    teams = json.loads(requests.get(
        'https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json').text)
    
    for team in teams:
        new_team = Team(
            team_id=team['teamId'],
            team_name=team['teamName']
        )
        db.session.add(new_team)
        db.session.commit()
        db.session.flush()

def undo_teams():
    db.session.execute('TRUNCATE teams CASCADE')
    db.session.commit()
