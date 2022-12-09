'''
Unit tests
'''

import pytest

from day09 import *

from . import __main__ as tmain


@pytest.fixture
def sample():
    return ['R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2']


@pytest.fixture
def parsed():
    return [('R', 4),
            ('U', 4),
            ('L', 3),
            ('D', 1),
            ('R', 4),
            ('D', 1),
            ('L', 5),
            ('R', 2)]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed


def test_move_head(parsed):
    head = [0, 0]

    for _ in range(parsed[0][1]):
        head = move_head(parsed[0], head)
    assert head == [0, 4]

    for _ in range(parsed[1][1]):
        head = move_head(parsed[1], head)
    assert head == [-4, 4]

    for _ in range(parsed[2][1]):
        head = move_head(parsed[2], head)
    assert head == [-4, 1]


def test_move_tail():
    tail = [0, 0]

    head = [0, 1]
    tail = move_tail(head, tail)
    assert tail == [0, 0]

    head = [0, 2]
    tail = move_tail(head, tail)
    assert tail == [0, 1]

    head = [1, 2]
    tail = move_tail(head, tail)
    assert tail == [0, 1]

    head = [2, 2]
    tail = move_tail(head, tail)
    assert tail == [1, 2]
