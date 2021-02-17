from .db import db


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer)
    team_name = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "team_name": self.team_name
        }
