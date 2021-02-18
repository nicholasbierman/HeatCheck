from flask import Blueprint
from app.models import League_Average

league_average_routes = Blueprint("league_averages", __name__)

@league_average_routes.route('/')
def get_all_league_averages():
    averages = League_Average.query.all()
    return {"league_averages": [average.to_dict() for average in averages]}