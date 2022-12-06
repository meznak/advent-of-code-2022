'''
Advent of Code 2022 Day 02
Rock, Paper, Scissors
'''

SAMPLE_SOLUTIONS = [15, 12]

# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

throws = {
    'A': {
        'name': 'rock',
        'win': 'C',
        'lose': 'B',
        'points': 1
    },
    'B': {
        'name': 'paper',
        'win': 'A',
        'lose': 'C',
        'points': 2
    },
    'C': {
        'name': 'scissors',
        'win': 'B',
        'lose': 'A',
        'points': 3
    },
    'X': {
        'name': 'rock',
        'win': 'C',
        'lose': 'B',
        'points': 1
    },
    'Y': {
        'name': 'paper',
        'win': 'A',
        'lose': 'C',
        'points': 2
    },
    'Z': {
        'name': 'scissors',
        'win': 'B',
        'lose': 'A',
        'points': 3
    }
}


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            output.append((item[0], item[2]))

    return output


def score_round(data: tuple) -> int:
    '''Determine result of round'''
    score = throws[data[1]]['points']

    if throws[data[1]]['win'] == data[0]:
        # win
        score += 6
    elif throws[data[1]]['lose'] == data[0]:
        # lose
        score += 0
    else:
        # draw
        score += 3

    return score


def score_decoded(data: tuple) -> int:
    '''
    Decode and determine result of round

    X: lose
    Y: draw
    Z: win
    '''

    if data[1] == 'X':
        play = throws[data[0]]['win']
        score = 0
    elif data[1] == 'Y':
        play = data[0]
        score = 3
    else:
        play = throws[data[0]]['lose']
        score = 6

    score += throws[play]['points']

    return score


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    score = 0

    for item in dataset:
        score += score_round(item)

    return score


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    score = 0

    for item in dataset:
        score += score_decoded(item)

    return score
