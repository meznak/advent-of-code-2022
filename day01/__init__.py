# TODO: Add day and title
'''
Advent of Code 2022 Day 01
Calorie Counting
'''

# TODO: Add sample solutions
SAMPLE_SOLUTIONS = [24000, 45000]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            output.append(int(item))
        else:
            output.append(None)

    return output


def sum_calories(dataset: list) -> list:
    '''Sum each elf's calories'''

    output = []

    elf = 0

    for item in dataset:
        if item is not None:
            elf += item
        else:
            output.append(elf)
            elf = 0

    return output


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    calorie_sums = sum_calories(dataset)
    return max(calorie_sums)


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    calorie_sums = sum_calories(dataset)
    calorie_sums.sort()

    return sum(calorie_sums[-3:])
