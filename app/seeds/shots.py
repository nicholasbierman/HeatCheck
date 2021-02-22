from app.models import db, Shot


def seed_shots():
    shot3 = Shot(nba_player_id=201939, x=250, y=60,
                 shot_zone="paint", shot_made_flag=1)
    shot1 = Shot(nba_player_id=201939, x=200, y=250,
                 shot_zone="paint",
                 shot_made_flag=1)
    shot2 = Shot(nba_player_id=201939, x=250, y=350,
                 shot_zone="paint",
                 shot_made_flag=1)
    shot4 = Shot(nba_player_id=201939, x=300, y=250,
                 shot_zone="paint",
                 shot_made_flag=1)
    shot4 = Shot(nba_player_id=201939, x=470, y=0,
                 shot_zone="Right Corner 3",
                 shot_made_flag=1)
    shot5 = Shot(nba_player_id=201939, x=10, y=0,
                 shot_zone="Left Corner 3", shot_made_flag=1)
    shot7 = Shot(nba_player_id=201939, x=250, y=250,
                 shot_zone="Back Court", shot_made_flag=1)
    shot8 = Shot(nba_player_id=201939, x=300, y=170, shot_made_flag=0,
                 shot_zone="Mid-Range - Right Side(R)")
    shot9 = Shot(nba_player_id=201939, x=50, y=170,
                 shot_zone="Mid-Range - Left Side(R)", shot_made_flag=0)
    shot10 = Shot(nba_player_id=201939, x=250, y=170,
                  shot_zone="Mid-Range - Center(C)", shot_made_flag=0)
    shot11 = Shot(nba_player_id=201939, x=220, y=170,
                  shot_zone="Mid-Range - Left Center(LC)",
                  shot_made_flag=0)
    shot12 = Shot(nba_player_id=201939, x=280, y=170,
                  shot_zone="Mid-Range - Right Center(RC)",
                  shot_made_flag=0)
    shot13 = Shot(nba_player_id=201939, x=250, y=250,
                  shot_zone="Above the Break 3 - Center(C)",
                  shot_made_flag=0)
    shot14 = Shot(nba_player_id=201939, x=300, y=260,
                  shot_zone="Above the Break 3 - Right Center(RC)",
                  shot_made_flag=0)
    shot15 = Shot(nba_player_id=201939, x=220, y=250,
                  shot_zone="Above the Break 3 - Left Center(LC)")
    shots = {shot1, shot2, shot3, shot4, shot5, shot7, shot8,
             shot10, shot11, shot12, shot13, shot14, shot15}
    for shot in shots:
        db.session.add(shot)
        db.session.commit()
        db.session.flush()


def undo_shots():
    db.session.execute('TRUNCATE shots CASCADE')
    db.session.commit()
