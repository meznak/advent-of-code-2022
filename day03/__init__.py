# TODO: Add day and title
'''
Advent of Code 2022 Day XX
TITLE
'''

# TODO: Add sample solutions
SAMPLE_SOLUTIONS = [157, 70]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    return dataset[:-1]


def split_lines(dataset: list) -> list:

    output = []

    for item in dataset:
        if item != '':
            mid = len(item)//2
            output.append((item[:mid], item[mid:]))

    return output


def prioritize(item: str) -> int:
    '''Convert an item label to its priority'''

    value = [ord(label) for label in item][0]

    if value >= 97:
        value -= 96
    else:
        value -= 38

    return value


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    priority_sum = 0

    knapsacks = split_lines(dataset)

    for item in knapsacks:
        dupe = set(item[0]).intersection(item[1])
        priority_sum += prioritize(dupe)

    return priority_sum


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    priority_sum = 0

    for group in range(0, len(dataset), 3):
        badge = set(dataset[group]).intersection(dataset[group+1]).intersection(dataset[group+2])

        priority_sum += prioritize(badge)

    return priority_sum