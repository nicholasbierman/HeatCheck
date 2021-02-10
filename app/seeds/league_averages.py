from app.models import db, League_Average


def seed_league_averages():
    a = League_Average(shot_zone_basic="Above the Break 3",
                       shot_zone_area="Center(C)",
                       shot_zone_range="24+ ft.",
                       fga=5026,
                       fgm=1751,
                       fg_pct=0.348
                       )

    b = League_Average(shot_zone_basic="Above the Break 3",
                       shot_zone_area="Back Court(BC)",
                       shot_zone_range="Back Court Shot",
                       fga=11,
                       fgm=0,
                       fg_pct=0.0,
                       )

    c = League_Average(shot_zone_basic="Above the Break 3",
                       shot_zone_area="Left Side Center(LC)",
                       shot_zone_range="24+ ft.",
                       fga=7001,
                       fgm=2589,
                       fg_pct=0.37
                       )

    d = League_Average(shot_zone_basic="Above the Break 3",
                       shot_zone_area="Right Side Center(RC)",
                       shot_zone_range="24+ ft.",
                       fga=6566,
                       fgm=2384,
                       fg_pct=0.363
                       )
    e = League_Average(shot_zone_basic="Backcourt",
                       shot_zone_area="Back Court(BC)",
                       shot_zone_range="Back Court Shot",
                       fga=103,
                       fgm=1,
                       fg_pct=0.01
                       )
    f = League_Average(shot_zone_basic="In The Paint (Non-RA)",
                       shot_zone_area="Center(C)",
                       shot_zone_range="8-16 ft.",
                       fga=3648,
                       fgm=1546,
                       fg_pct=0.446
                       )
    g = League_Average(shot_zone_basic="In The Paint (Non-RA)",
                       shot_zone_area="Center(C)",
                       shot_zone_range="Less than 8 ft.",
                       fga=6045,
                       fgm=2495,
                       fg_pct=0.413
                       )
    h = League_Average(shot_zone_basic="In The Paint (Non-RA)",
                       shot_zone_area="Left Side(L)",
                       shot_zone_range="8-16 ft.",
                       fga=575,
                       fgm=232,
                       fg_pct=0.403
                       )
    i = League_Average(shot_zone_basic="In The Paint (Non-RA)",
                       shot_zone_area="Right Side(R)",
                       shot_zone_range="8-16 ft.",
                       fga=631,
                       fgm=262,
                       fg_pct=0.415
                       )

    j = League_Average(shot_zone_basic="Left Corner 3",
                       shot_zone_area="Left Side(L)",
                       shot_zone_range="24+ ft.",
                       fga=3071,
                       fgm=1248,
                       fg_pct=0.406
                       )

    k = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Center(C)",
                       shot_zone_range="8-16 ft",
                       fga=675,
                       fgm=303,
                       fg_pct=0.499
                       )

    l = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Center(C)",
                       shot_zone_range="16-24 ft.",
                       fga=1386,
                       fgm=591,
                       fg_pct=0.426
                       )

    m = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Left Side Center(LC)",
                       shot_zone_range="16-24 ft.",
                       fga=1175,
                       fgm=482,
                       fg_pct=0.41
                       )

    n = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Left Side(L)",
                       shot_zone_range="16-24 ft",
                       fga=499,
                       fgm=199,
                       fg_pct=0.399
                       )

    o = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Left Side(L)",
                       shot_zone_range="8-16 ft.",
                       fga=1384,
                       fgm=553,
                       fg_pct=0.4
                       )

    p = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Right Side(R)",
                       shot_zone_range="16-24 ft.",
                       fga=442,
                       fgm=172,
                       fg_pct=0.394
                       )

    q = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Right Side(R)",
                       shot_zone_range="8-16 ft",
                       fga=1402,
                       fgm=584,
                       fg_pct=0.417
                       )

    r = League_Average(shot_zone_basic="Mid-Range",
                       shot_zone_area="Right Side Center(RC)",
                       shot_zone_range="16-24 ft.",
                       fga=1217,
                       fgm=508,
                       fg_pct=0.417
                       )

    s = League_Average(shot_zone_basic="Restricted Area",
                       shot_zone_area="Center(C)",
                       shot_zone_range="Less Than 8 ft.",
                       fga=18931,
                       fgm=11829,
                       fg_pct=0.625
                       )

    t = League_Average(shot_zone_basic="Right Corner 3",
                       shot_zone_area="Right Side(R)",
                       shot_zone_range="24+ ft.",
                       fga=2800,
                       fgm=1080,
                       fg_pct=0.386
                       )
    dict = {a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t}
    for letter in dict:
        db.session.add(letter)
        db.session.commit()
        db.session.flush()


def undo_league_averages():
    db.session.execute('TRUNCATE league_averages CASCADE')
    db.session.commit()
