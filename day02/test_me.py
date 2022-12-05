'''
Unit tests
'''

from day02 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['A Y', 'B X', 'C Z', '']


@pytest.fixture
def parsed():
    return [('A', 'Y'), ('B', 'X'), ('C', 'Z')]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    result = parse_data(sample)

    assert result == parsed


def test_score_round(parsed):
    assert score_round(parsed[0]) == 8
    assert score_round(parsed[1]) == 1
    assert score_round(parsed[2]) == 6


def test_score_decoded(parsed):
    assert score_decoded(parsed[0]) == 4
    assert score_decoded(parsed[1]) == 1
    assert score_decoded(parsed[2]) == 7

