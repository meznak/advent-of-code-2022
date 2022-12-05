'''
Unit tests
'''


from day03 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']


@pytest.fixture
def halved():
    return [('vJrwpWtwJgWr', 'hcsFMMfFFhFp'), ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'), ('PmmdzqPrV', 'vPwwTWBwg'), ('wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'), ('ttgJtRGJ', 'QctTZtZT'), ('CrZsJsPPZsGz', 'wwsLwLmpwMDw')]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_input(sample):
    assert parse_data(sample) == sample[:-1]


def test_split_lines(sample, halved):
    assert split_lines(sample) == halved


def test_prioritize():
    items = [('p', 16), ('L', 38), ('P', 42), ('v', 22), ('t', 20), ('s', 19)]

    for item in items:
        assert prioritize(item[0]) == item[1]