from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
import json
import requests

response = shotchartdetail.ShotChartDetail(
    team_id=0, player_id=201939, season_nullable='2020-21', season_type_all_star='Regular Season'
    )

shots = response.get_json()

content = json.loads(shots)

print(content)
