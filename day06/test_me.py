'''
Unit tests
'''

from day06 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']


@pytest.fixture
def parsed():
    return ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_input(sample, parsed):
    assert parse_data(sample) == parsed
