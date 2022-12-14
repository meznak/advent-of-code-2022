'''
Advent of Code 2022 Day 12
Hill Climbing Algorithm
'''

from copy import deepcopy
from shared.helpers import get_neighbors
from shared.node import Node


SAMPLE_SOLUTIONS = [31, 29]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        output.append([ord(char) for char in list(item)])

    return output


def find_endpoints(grid: list) -> tuple:
    '''Detect the nodes marked as start and end'''

    start = [None, None]
    end = [None, None]

    for index, row in enumerate(grid):
        try:
            start[1] = row.index(83)  # 'S'
            start[0] = index
        except ValueError:
            pass

    for index, row in enumerate(grid):
        try:
            end[1] = row.index(69)  # 'E'
            end[0] = index
        except ValueError:
            pass

    return (tuple(start), tuple(end))


def bfs(grid: list, goal_value: int, root: Node,
        ascend: bool, goal_position=None) -> list:
    '''Breadth-first search'''

    queue = [root]

    root.visited = True

    while len(queue) > 0:
        current = queue.pop(0)

        if current.value == goal_value:
            if goal_position is None or \
                    (goal_position is not None and
                     current.position == goal_position):
                break
        neighbors = get_neighbors(grid, current.position)
        for neighbor_position in neighbors:
            neighbor = grid[neighbor_position[0]][neighbor_position[1]]
            if not neighbor.visited and \
                    ((ascend and neighbor.value <= current.value + 1) or
                     (not ascend and neighbor.value >= current.value - 1)):
                neighbor.visited = True
                neighbor.parent = current
                queue.append(neighbor)

    # Build list by backtracking
    path = [current.position]

    while current != root:
        current = current.parent
        path.append(current.position)

    # Return the reversed path
    return path[::-1]


def show_result(dataset: list, path: list) -> None:
    '''Graphically display the result'''

    grid = [[chr(height) for height in row] for row in dataset]

    for point in path:
        grid[point[0]][point[1]] = grid[point[0]][point[1]].capitalize()

    print('\n'.join([''.join(line) for line in grid]))


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    endpoints = find_endpoints(dataset)

    # Temporarily change the endpoint heights
    dataset[endpoints[0][0]][endpoints[0][1]] = ord('a')
    dataset[endpoints[1][0]][endpoints[1][1]] = ord('z')

    grid = [[Node(height, None, (row_num, col_num)) for
            col_num, height in enumerate(row)] for
            row_num, row in enumerate(dataset)]
    path = bfs(grid, ord('z'), grid[endpoints[0][0]][endpoints[0][1]],
               ascend=True, goal_position=endpoints[1])

    # Restore the endpoint heights
    dataset[endpoints[0][0]][endpoints[0][1]] = ord('S')
    dataset[endpoints[1][0]][endpoints[1][1]] = ord('E')

    show_result(dataset, path)

    # No step to reach the starting position
    return len(path) - 1


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    endpoints = find_endpoints(dataset)

    # Temporarily change the endpoint heights
    dataset[endpoints[0][0]][endpoints[0][1]] = ord('a')
    dataset[endpoints[1][0]][endpoints[1][1]] = ord('z')

    grid = [[Node(height, None, (row_num, col_num)) for
            col_num, height in enumerate(row)] for
            row_num, row in enumerate(dataset)]
    path = bfs(grid, ord('a'), grid[endpoints[1][0]][endpoints[1][1]],
               ascend=False)

    # Restore the endpoint heights
    dataset[endpoints[0][0]][endpoints[0][1]] = ord('S')
    dataset[endpoints[1][0]][endpoints[1][1]] = ord('E')

    show_result(dataset, path)

    # No step to reach the starting position
    return len(path) - 1
