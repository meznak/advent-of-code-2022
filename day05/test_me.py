'''
Unit tests
'''

from day05 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['    [D]', '[N] [C]', '[Z] [M] [P]', ' 1   2   3', '', 'move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']


@pytest.fixture
def raw_stacks():
    return [[' ', 'D', ' '],
            ['N', 'C', ' '],
            ['Z', 'M', 'P']]


@pytest.fixture
def parsed():
    return [[['Z', 'N'], ['M', 'C', 'D'], ['P']], [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_input(sample, parsed):
    assert parse_data(sample) == parsed


def test_transpose_stacks(raw_stacks, parsed):
    assert transpose_stacks(raw_stacks) == parsed[0]


def test_move_crates(parsed):
    move_crates(parsed)

    assert parsed[0] == [['C'], ['M'], ['P', 'D', 'N', 'Z']]


def test_move_multi_crates(parsed):
    move_multi_crates(parsed)

    assert parsed[0] == [['M'], ['C'], ['P', 'Z', 'N', 'D']]
