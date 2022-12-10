'''
Advent of Code 2022 Day 10
Cathode-Ray Tube
'''

SAMPLE_SOLUTIONS = [13140, '''##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
''']


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item == 'noop':
            output.append((0, 0))
        else:
            _, param = item.split(' ')
            output.append((1, int(param)))

    return output


def addx(clock: int, register: int, param: int) -> tuple:
    '''Add a paraamter and register'''
    return (clock + 2, register + param)


def noop(clock: int) -> int:
    '''Do nothing but advance the clock'''
    return clock + 1


def check_clock(clock: int, oper: int) -> tuple:
    '''Determine whether the current cycle is interesting'''

    if clock == 20 or (clock - 20) % 40 == 0:
        return (True, 0)
    elif oper == 1 and \
            (clock == 21 or (clock - 20) % 40 == 1):
        # 20th cycle occurred mid-add
        return (True, 1)
    else:
        return (False, 0)


def check_draw(clock: int, cursor: int, oper: int) -> tuple:
    '''Determine whether a pixel should be drawn'''

    clock %= 40

    # First pixel
    if cursor - 1 <= clock <= cursor + 1:
        first_pixel = '#'
    else:
        first_pixel = '.'

    # Second pixel
    if oper == 1:
        clock = (clock + 1) % 40
        if cursor - 1 <= clock <= cursor + 1:
            second_pixel = '#'
        else:
            second_pixel = '.'

    else:
        second_pixel = ' '

    return (first_pixel, second_pixel)


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    clock = 0
    register_x = 1
    signal_sum = 0

    for item in dataset:
        oper_start_x = register_x

        oper = item[0]
        param = item[1]

        if oper == 0:
            clock = noop(clock)
        else:
            clock, register_x = addx(clock, register_x, param)

        interesting, offset = check_clock(clock, oper)

        if interesting:
            signal_sum += oper_start_x * (clock - offset)

    return signal_sum


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    clock = 0
    register_x = 1
    display = [' '] * 40 * 6

    for item in dataset:
        oper = item[0]
        param = item[1]

        first_pixel, second_pixel = check_draw(clock, register_x, oper)

        # Activate pixels
        display[clock] = first_pixel

        if oper == 1:
            display[clock + 1] = second_pixel

        if oper == 0:
            clock = noop(clock)
        else:
            clock, register_x = addx(clock, register_x, param)

    # Split display into lines
    output = []
    for i in range(0, 240, 40):
        output.append(display[i:i+40])
        output[-1].append('\n')

    output = ''.join([''.join(line) for line in output])

    return output
