'''
Unit tests
'''

import pytest

# TODO: Change from skel to current day
from skel import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    return []


@pytest.fixture
def parsed():
    return []


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed
