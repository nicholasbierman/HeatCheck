from .db import db


class League_Average(db.Model):
    __tablename__ = "league_averages"

    id = db.Column(db.Integer, primary_key=True)
    shot_zone_basic = db.Column(db.String(255))
    shot_zone_area = db.Column(db.String(255))
    shot_zone_range = db.Column(db.String(255))
    fga = db.Column(db.Integer, nullable=False)
    fgm = db.Column(db.Integer, nullable=False)
    fg_pct = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "shot_zone_basic": self.shot_zone_basic,
            "shot_zone_area": self.shot_zone_area,
            "shot_zone_range": self.shot_zone_range,
            "fga": self.fga,
            "fgm": self.fgm,
            "fg_pct": self.fg_pct
        }