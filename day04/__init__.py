'''
Advent of Code 2022 Day 04
Camp Cleanup
'''

SAMPLE_SOLUTIONS = [2, 4]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            elves = item.split(',')
            first = [int(i) for i in elves[0].split('-')]
            second = [int(i) for i in elves[1].split('-')]

            output.append(first + second)

    return output


def find_contains(dataset: list) -> list:
    '''Detect pairs that contain each others' range'''

    contains = []

    for item in dataset:
        # First contained in second or Second contained in first
        if (item[0] >= item[2] and item[1] <= item[3]) or \
                (item[0] <= item[2] and item[1] >= item[3]):
            contains.append(True)
        else:
            contains.append(False)

    return contains


def find_overlaps(dataset: list) -> list:
    '''Detect pairs that contain each others' range'''

    overlaps = []

    for item in dataset:
        # First contained in second or Second contained in first
        if (item[2] <= item[0] <= item[3]) or \
                (item[2] <= item[1] <= item[3]) or \
                (item[0] <= item[2] <= item[1]) or \
                (item[0] <= item[3] <= item[1]):
            overlaps.append(True)
        else:
            overlaps.append(False)

    return overlaps


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    return sum(find_contains(dataset))


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    return sum(find_overlaps(dataset))
