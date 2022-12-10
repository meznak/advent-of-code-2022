'''
Unit tests
'''

import pytest

from day10 import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    return ['noop',
            'addx 3',
            'addx -5']


@pytest.fixture
def parsed():
    return [(0, 0),
            (1, 3),
            (1, -5)]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed


def test_addx(parsed):
    assert addx(0, 1, parsed[1][1]) == (2, 4)
    assert addx(2, 4, parsed[2][1]) == (4, -1)


def test_noop():
    assert noop(0) == 1
    assert noop(10) == 11


def test_check_clock():
    assert check_clock(12, 0) == (False, 0)
    assert check_clock(20, 0) == (True, 0)
    assert check_clock(21, 1) == (True, 1)
    assert check_clock(140, 0) == (True, 0)
    assert check_clock(140, 1) == (True, 0)
    assert check_clock(141, 1) == (True, 1)


def test_check_draw():
    assert check_draw(0, 1, 1) == (True, True)
    assert check_draw(2, 16, 1) == (False, False)
    assert check_draw(4, 5, 1) == (True, True)
    assert check_draw(6, 11, 1) == (False, False)
    assert check_draw(18, 21, 0) == (False, False)
    assert check_draw(72, 34, 1) == (False, True)
