'''
Unit tests
'''

import pytest

from day12 import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    return ['Sabqponm',
            'abcryxxl',
            'accszExk',
            'acctuvwj',
            'abdefghi']


@pytest.fixture
def parsed():
    return [[83, 97, 98, 113, 112, 111, 110, 109],
            [97, 98, 99, 114, 121, 120, 120, 108],
            [97, 99, 99, 115, 122, 69, 120, 107],
            [97, 99, 99, 116, 117, 118, 119, 106],
            [97, 98, 100, 101, 102, 103, 104, 105]]


""" def test_main():
    '''Test main'''
    tmain.main() """


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed


def test_find_endpoints(parsed):
    assert find_endpoints(parsed) == ([0, 0], [2, 5])


def test_a_star(parsed):
    path = a_star(parsed, [(0, 0), (4, 3)])
    assert path == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3)]


def test_solve_2(parsed):
    solve_2(parsed)