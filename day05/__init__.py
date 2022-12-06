'''
Advent of Code 2022 Day 05
Supply Stacks
'''

from copy import deepcopy

SAMPLE_SOLUTIONS = ['CMZ', 'MCD']


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = [[], []]

    section = 0
    temp_stacks = []

    for item in dataset:
        if section == 0:
            # Stacks
            if item[1] != '1':
                temp_stacks.append([item[i] for i in range(1, len(item), 4)])
            else:
                # End of stack diagram
                output[0] = transpose_stacks(temp_stacks)

                section += 1
                continue

        elif item == '':
            continue
        else:
            # Instructions
            split_line = item.split(' ')
            instruction = [int(split_line[i]) for i in [1, 3, 5]]

            output[1].append(instruction)

    return output


def transpose_stacks(stacks: list) -> list:
    '''Enumerate each stack from the bottom'''

    output = []

    for j in range(len(stacks[-1])):
        stack = []
        for i in range(len(stacks) - 1, -1, -1):
            try:
                if stacks[i][j] != ' ':
                    stack.append(stacks[i][j])
            except IndexError:
                # Account for short stacks
                pass

        output.append(stack)

    return output


def move_crates(dataset: list) -> None:
    '''Move crates according to instructions'''

    for item in dataset[1]:
        count = item[0]
        source = item[1] - 1
        dest = item[2] - 1

        for _ in range(count):
            dataset[0][dest].append(dataset[0][source].pop())


def move_multi_crates(dataset: list) -> None:
    '''Move crates according to instructions
            Multiple crates at once'''

    for item in dataset[1]:
        count = item[0]
        source = item[1] - 1
        dest = item[2] - 1

        held = []

        for __ in range(count):
            held.insert(0, dataset[0][source].pop())

        dataset[0][dest] += held


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    local_dataset = deepcopy(dataset)

    move_crates(local_dataset)

    return ''.join([stack[-1] for stack in local_dataset[0]])


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    local_dataset = deepcopy(dataset)

    move_multi_crates(local_dataset)

    return ''.join([stack[-1] for stack in local_dataset[0]])