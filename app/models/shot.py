from .db import db


class Shot(db.Model):
    __tablename__ = "shots"

    id = db.Column(db.Integer, primary_key=True)
    nba_player_id = db.Column(
        db.Integer, db.ForeignKey("players.nba_player_id"))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    shot_zone = db.Column(db.String(255))
    shot_made_flag = db.Column(db.Boolean, nullable=False, default=True)

    def to_dict(self):
        return {
            "nba_player_id": self.nba_player_id,
            "shot_made_flag": self.shot_made_flag,
            "x": self.x,
            "y": self.y,
            "shot_zone": self.shot_zone
        }
