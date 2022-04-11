from src.location_blurb import y_to_lat
from math import isclose
from pytest import raises


def test_y_to_lat_zero():
    assert(y_to_lat(0) == 0)


def test_y_to_lat_symmetry():
    assert(isclose(y_to_lat(0.5), - y_to_lat(-0.5)))


def test_y_to_lat_correct():
    assert(isclose(y_to_lat(0.5), 0.480381079134))
    assert(isclose(y_to_lat(1.484), 1.12487737228))


def test_y_to_lat_bounds():
    with raises(Exception):
        y_to_lat(3.0)
