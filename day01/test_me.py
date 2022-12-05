'''
Unit tests
'''

import pytest

from day01 import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    return ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000', '']


@pytest.fixture
def parsed():
    return [1000, 2000, 3000, None, 4000, None, 5000, 6000, None, 7000, 8000, 9000, None, 10000, None]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample):
    result = parse_data(sample)

    assert result == [1000, 2000, 3000, None, 4000, None, 5000, 6000, None, 7000, 8000, 9000, None, 10000, None]


def test_sum_calories(parsed):
    result = sum_calories(parsed)

    assert result == [6000, 4000, 11000, 24000, 10000]
