'''
Advent of Code 2022 Day 09
Rope Bridge
'''

SAMPLE_SOLUTIONS = [13, 36]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        terms = item.split(' ')
        output.append((terms[0], int(terms[1])))

    return output


def move_head(move: list, head: list) -> list:
    '''Move the head according to instructions'''
    if move[0] == 'U':
        head[0] -= 1
    if move[0] == 'D':
        head[0] += 1
    if move[0] == 'L':
        head[1] -= 1
    if move[0] == 'R':
        head[1] += 1

    return head


def move_tail(head: list, tail: list) -> list:
    '''Make the tail follow the head'''

    while True:
        dy = head[0] - tail[0]
        dx = head[1] - tail[1]

        if abs(dy) < 2 and abs(dx) < 2:
            break

        if abs(dy) == abs(dx):
            # Move diagonally
            tail[0] += dy // 2
            tail[1] += dx // 2

        elif abs(dy) > 1:
            if dx == 0:
                # Same column; just follow.
                tail[0] += dy // 2
            else:
                # Move diagonally
                tail[0] += dy // 2
                tail[1] += dx

        elif abs(dx) > 1:
            if dy == 0:
                # Same row; just follow.
                tail[1] += dx // 2
            else:
                # Move diagonally
                tail[0] += dy
                tail[1] += dx // 2

    return tail


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    head = [0, 0]
    tail = [0, 0]

    tail_visits = set()

    for item in dataset:
        for _ in range(item[1]):
            head = move_head(item, head)
            tail = move_tail(head, tail)
            tail_visits.add(tuple(tail))

    return len(tail_visits)


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    rope = []
    for _ in range(10):
        rope.append([0, 0])

    tail_visits = set()

    for item in dataset:
        for _ in range(item[1]):
            rope[0] = move_head(item, rope[0])
            for knot in range(9):
                rope[knot + 1] = move_tail(rope[knot], rope[knot + 1])

            tail_visits.add(tuple(rope[-1]))

    return len(tail_visits)