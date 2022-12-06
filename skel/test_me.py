'''
Unit tests
'''

from skel import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return []


@pytest.fixture
def parsed():
    return []


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_input(sample):
    assert parse_data(sample) == sample[:-1]