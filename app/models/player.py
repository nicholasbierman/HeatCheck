from .db import db


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    nba_player_id = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "nba_player_id": self.nba_player_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "team_id": self.team_id
        }
