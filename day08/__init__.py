'''
Advent of Code 2022 Day 08
Treetop Tree House
'''

SAMPLE_SOLUTIONS = [21, 8]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        row = [int(tree) for tree in item]
        output.append(row)

    return output


def check_visible(dataset: list, direction: str, visible: set) -> None:
    '''Count visible trees from a given side'''

    rows = len(dataset)
    cols = len(dataset[0])

    if direction in ('down', 'up'):
        if direction == 'down':
            # from top
            row_range = range(rows)
            col_range = range(cols)
        else:
            # from bottom
            row_range = range(rows - 1, -1, -1)
            col_range = range(cols - 1, -1, -1)

        for col in col_range:
            tallest = -1
            for row in row_range:
                height = dataset[row][col]
                if height > tallest:
                    visible.add((row, col))
                    tallest = height

    else:
        if direction == 'right':
            # from the left
            row_range = range(rows)
            col_range = range(cols)
        else:
            # from the right
            row_range = range(rows - 1, -1, -1)
            col_range = range(cols - 1, -1, -1)

        for row in row_range:
            tallest = -1
            for col in col_range:
                height = dataset[row][col]
                if height > tallest:
                    visible.add((row, col))
                    tallest = height


def check_view(dataset: list, position: tuple) -> int:
    '''Calculate a tree's view score'''

    rows = len(dataset)
    cols = len(dataset[0])

    tree_height = dataset[position[0]][position[1]]

    distances = [0, 0, 0, 0]

    # Check column
    col = position[1]
    # down
    for row in range(position[0] + 1, rows):
        height = dataset[row][col]
        distances[0] += 1
        if height >= tree_height:
            break

    # up
    for row in range(position[0] - 1, -1, -1):
        height = dataset[row][col]
        distances[1] += 1
        if height >= tree_height:
            break

    # Check row
    row = position[0]
    # left
    for col in range(position[1] - 1, -1, -1):
        height = dataset[row][col]
        distances[2] += 1
        if height >= tree_height:
            break

    # right
    for col in range(position[1] + 1, cols):
        height = dataset[row][col]
        distances[3] += 1
        if height >= tree_height:
            break

    score = 1
    for distance in distances:
        score *= distance

    return score


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    visible = set()

    check_visible(dataset, 'down', visible)
    check_visible(dataset, 'left', visible)
    check_visible(dataset, 'up', visible)
    check_visible(dataset, 'right', visible)

    return len(visible)


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    rows = len(dataset)
    cols = len(dataset[0])
    visibility_scores = []

    for row in range(rows):
        row_scores = []
        for col in range(cols):
            row_scores.append(check_view(dataset, (row, col)))

        visibility_scores.append(row_scores)

    return max([max(row) for row in visibility_scores])
