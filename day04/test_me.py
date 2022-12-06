'''
Unit tests
'''

from day04 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


@pytest.fixture
def parsed():
    return [[2, 4, 6, 8], [2, 3, 4, 5], [5, 7, 7, 9], [2, 8, 3, 7], [6, 6, 4, 6], [2, 6, 4, 8]]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_input(sample, parsed):
    assert parse_data(sample) == parsed


def test_find_contains(parsed):
    assert find_contains(parsed) == [False, False, False, True, True, False]


def test_find_overlaps(parsed):
    assert find_overlaps(parsed) == [False, False, True, True, True, True]
