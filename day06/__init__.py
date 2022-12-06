'''
Advent of Code 2022 Day 06
Tuning Trouble
'''

SAMPLE_SOLUTIONS = [7, 19]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    return dataset


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    data = dataset[0]
    data_length = len(data)

    for i in range(4, data_length):
        if len(set(data[i-4:i])) == 4:
            # Found a marker
            return i


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    data = dataset[0]
    data_length = len(data)

    for i in range(14, data_length):
        if len(set(data[i-14:i])) == 14:
            # Found a marker
            return i