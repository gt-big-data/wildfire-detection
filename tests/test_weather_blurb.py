from src.weather_blurb import json_to_blurb, deg_to_dir


def test_json_to_blurb():
    pass


def test_deg_to_dir():
    assert(deg_to_dir(0) == 'N')
    assert(deg_to_dir(360) == 'N')
    assert(deg_to_dir(90) == 'E')
    assert(deg_to_dir(45) == 'NE')
    assert(deg_to_dir(240.2) == 'WSW')
    assert(deg_to_dir(11.25) == 'N')
