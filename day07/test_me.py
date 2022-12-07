'''
Unit tests
'''

from day07 import *

from . import __main__ as tmain

import pytest


@pytest.fixture
def sample():
    return ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

@pytest.fixture
def parsed():
    return [{'/': {
            'a': {
                'e': {
                    'i': 584
                },
                'f': 29116,
                'g': 2557,
                'h.lst': 62596
            },
            'b.txt': 14848514,
            'c.dat': 8504156,
            'd': {
                'j': 4060174,
                'd.log': 8033020,
                'd.ext': 5626152,
                'k': 7214296
            }
            }}]


@pytest.fixture
def sizes():
    return [[[584], 94269], [24933642], 23352670]


def test_main():
    '''Test main'''
    tmain.main()


def test_parse_data(sample, parsed):
    assert parse_data(sample) == parsed


def test_parse_command():
    assert parse_command('$ cd /') == ['cd', '/']
    assert parse_command('$ cd a') == ['cd', 'a']
    assert parse_command('$ cd ..') == ['cd', '..']
    assert parse_command('$ ls') == ['ls']


def test_cd(parsed):
    tree = parsed[0]

    dirs = ['/']
    cwd = tree[dirs[0]]

    cwd = cd(tree, dirs, cwd, 'a')
    assert cwd == tree['/']['a']

    cwd = cd(tree, dirs, cwd, 'new')
    assert cwd == tree['/']['a']['new']

    cwd = cd(tree, dirs, cwd, '..')
    assert cwd == tree['/']['a']


def test_find_dir_sizes(parsed, sizes):
    tree = parsed[0]

    assert find_dir_sizes(tree['/']) == sizes


def test_sum_dir_sizes(sizes):
    assert sum_dir_sizes(sizes) == [584, 94853, 24933642, 48381165]
