'''
Shared library for AoC20xx solutions
'''

import os
import timeit
from typing import Callable, List, Tuple


def read_input(script_file: str, strip=True) -> Tuple[list]:
    '''
    Read sample and puzzle input files
    '''

    path = os.path.dirname(os.path.realpath(script_file))

    sample_file = os.path.join(path, 'sample1')
    with open(sample_file, 'r') as in_file:
        if strip:
            sample_1 = [entry.strip() for entry in in_file.readlines()]
        else:
            sample_1 = [entry.strip('\n') for entry in in_file.readlines()]
        #sample_1.append('')

    try:
        sample_file = os.path.join(path, 'sample2')
        if os.stat(sample_file).st_size > 0:
            with open(sample_file, 'r') as in_file:
                if strip:
                    sample_2 = [entry.strip() for entry in in_file.readlines()]
                else:
                    sample_2 = [entry.strip('\n') for entry in in_file.readlines()]
                #sample_2.append('')
        else:
            sample_2 = sample_1
    except FileNotFoundError:
        sample_2 = sample_1
        print('sample2 file not found')

    samples = [sample_1, sample_2]

    with open(os.path.join(path, 'input'), 'r') as in_file:
        if strip:
            data = [entry.strip() for entry in in_file.readlines()]
        else:
            data = [entry.strip('\n') for entry in in_file.readlines()]
        #data.append('')

    return (samples, data)


def parse_input(script_file: str, parse_data: Callable[[], list], strip=True) -> tuple:
    '''Read and parse data'''
    samples, data = read_input(script_file, strip)

    samples_parsed = [parse_data(sample) for sample in samples]
    data_parsed = parse_data(data)

    return samples_parsed, data_parsed


def solve_list(sample: List[str], data: List[str], solve: Callable[[list], int],
               sample_solution: int) -> int:
    '''
    Run solution against sample data, comparing expected results. If
    satisfactory, run solution against puzzle data.
    '''

    run_count = 0

    for dataset in [sample, data]:
        start = timeit.default_timer()
        result = solve(dataset)
        stop = timeit.default_timer()
        print(f'Time: {stop - start:.9f} seconds')

        if run_count == 0:
            try:
                assert(result == sample_solution), \
                    f'''Expected {sample_solution}, got {result}'''
                print('test PASSED')
            except AssertionError as err:
                print(f'test FAILED')
            run_count += 1

    return result


def run_solvers(samples: list, data: list, solvers: list,
                sample_solutions: list) -> None:
    '''
    Run all solutions for the current puzzle
    '''

    for index, _ in enumerate(sample_solutions):
        result = solve_list(samples[index], data, solvers[index],
                            sample_solutions[index])
        print(f'result {index}: {result}')
