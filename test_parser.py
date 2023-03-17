from parser import *
import pytest


@pytest.fixture
def udp_message():
    return "m0f6!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


@pytest.fixture
def json():
    my_json = {"regular": [0, 0], "forward": [0, 0], "last_event": "test"}
    return my_json

def test_forward_update_stats(json):
    assert update_stats(1, 0, json)['forward'] == [0, 1]


def test_regular_update_stats(json):
    assert update_stats(1, 1, json)['regular'] == [0, 1]


def test_regular_update_last_event():
    assert update_last_event(1, 1) == "New message received by meter 1. Content from meter 1"


def test_forward_update_last_event():
    assert update_last_event(1, 0) == "New message forwarded by meter 0. Content from meter 1"


def test_parse_message(udp_message):
    m_number, f_number = parse_message(udp_message)
    assert m_number == 0
    assert f_number == 6


def test_parse_message_invalid_m():
    msg = "mzf3"
    m_number, f_number = parse_message(msg)
    assert m_number is None
    assert f_number == 3


def test_parse_message_invalid_f():
    msg = "m2f"
    m_number, f_number = parse_message(msg)
    assert m_number == 2
    assert f_number is None


def test_update_stats_regular():
    _json = {
        "regular": [0, 0],
        "forward": [0, 0],
        "last_event": ""
    }
    generator = 1
    forwarder = 1

    updated_json = update_stats(generator, forwarder, _json)
    assert updated_json["regular"] == [0, 1]
    assert updated_json["forward"] == [0, 0]


def test_update_stats_forward():
    _json = {
        "regular": [0, 0],
        "forward": [0, 0],
        "last_event": ""
    }
    generator = 1
    forwarder = 0

    updated_json = update_stats(generator, forwarder, _json)
    assert updated_json["regular"] == [0, 0]
    assert updated_json["forward"] == [0, 1]
