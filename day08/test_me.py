'''
Unit tests
'''

from day08 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['30373', '25512', '65332', '33549', '35390']


@pytest.fixture
def parsed():
    return [[3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0]]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed


def test_check_visible(parsed):
    down = set()
    check_visible(parsed, 'down', down)
    assert len(down) == 10

    left = set()
    check_visible(parsed, 'left', left)
    assert len(left) == 11


def test_check_view(parsed):
    assert check_view(parsed, (1, 2)) == 4
    assert check_view(parsed, (3, 2)) == 8
