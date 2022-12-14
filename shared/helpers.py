'''Helper functions'''

from .node import Node


def a_star(grid: list, endpoints: list) -> list:
    '''A* Pathfinding'''

    start = Node(grid[endpoints[0][0]][endpoints[0][1]], None, endpoints[0])
    end = Node(grid[endpoints[1][0]][endpoints[1][1]], None, endpoints[1])

    start.f = 0
    start.g = 0

    start.h = (end.position[0] - start.position[0]) + \
              (end.position[1] - start.position[1])

    # Initialize open and closed lists
    open_list = [start]
    closed_list = []

    while len(open_list) > 0:
        # Choose the open node with the lowest f value
        open_list.sort(key=lambda node: node.f)
        current = open_list.pop(0)
        if current in closed_list:
            continue

        # Close the current node
        closed_list.append(current)

        if current == end:
            # Goal reached
            break

        # Create children
        children = []

        neighbors = get_neighbors(grid, current.position)

        for neighbor in neighbors:
            neighbor_height = grid[neighbor[0]][neighbor[1]]
            if neighbor_height <= current.value + 1:
                new_node = Node(neighbor_height, current,
                                (neighbor[0], neighbor[1]))
                if new_node not in closed_list:
                    children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            # From start via current
            distance = abs(child.position[0] - current.position[0]) + \
                abs(child.position[1] - current.position[1])
            child.g = current.g + distance

            # From end
            distance = abs(end.position[0] - child.position[0]) + \
                abs(end.position[1] - child.position[1])
            child.h = distance

            # Total cost
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    break
            else:
                open_list.append(child)

    # Build list by backtracking
    path = [current.position]

    while current != start:
        current = current.parent
        path.append(current.position)

    # Return the reversed path
    return path[::-1]


def get_neighbors(grid: list, current_position: tuple) -> list:
    '''Return a list of a position's neighbors'''

    row_count = len(grid)
    col_count = len(grid[0])
    neighbors = []

    for offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        neighbor_y = current_position[0] + offset[0]
        if not 0 <= neighbor_y < row_count:
            continue

        neighbor_x = current_position[1] + offset[1]
        if not 0 <= neighbor_x < col_count:
            continue

        neighbors.append((neighbor_y, neighbor_x))

    return neighbors
