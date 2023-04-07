from parser import *
import pytest


def test_extract_meter_data(udp_message):
    assert extract_meter_data("m3f4ffffffffffffffffffff") == 3, 4

def test_check_forward(udp_message):
    assert True


def test_update_stats():
    assert False