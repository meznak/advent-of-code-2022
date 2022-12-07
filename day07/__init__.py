'''
Advent of Code 2022 Day 07
No Space Left On Device
'''

SAMPLE_SOLUTIONS = [95437, 24933642]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    tree = {}

    dirs = []
    cwd = tree

    for item in dataset:
        if item[0] == '$':
            # Command
            cmd = parse_command(item)

            if cmd[0] == 'cd':
                # Change directory

                cwd = cd(tree, dirs, cwd, cmd[1])
            else:
                # List contents
                # Handled in outer else
                pass
        else:
            size, name = item.split(' ')
            if size == 'dir':
                cwd[name] = {}
            else:
                cwd[name] = int(size)

    return [tree]


def parse_command(cmd: str) -> list:
    '''Interpret a command'''

    return cmd.split(' ')[1:]


def cd(tree: dict, dirs: list, cwd: dict, dest: str) -> dict:
    '''Change directory'''

    if dest == '..':
        # Go up a directory
        dirs.pop()
        dest = dirs[-1]
        cwd = tree

        for dir_name in dirs:
            cwd = cwd[dir_name]

    else:
        # Descend a directory
        dirs.append(dest)
        if dest not in cwd:
            cwd[dest] = {}

        cwd = cwd[dest]

    return cwd


def find_dir_sizes(tree) -> int:
    '''Calculate directory sizes'''

    output = []

    tree_size = 0

    for filename in tree:
        if isinstance(tree[filename], dict):
            subdirs = find_dir_sizes(tree[filename])
            output.append([subdir for subdir in subdirs])

        else:
            tree_size += tree[filename]

    return output + [tree_size]


def sum_dir_sizes(dirs: list) -> list:
    '''Calculate directory sizes including subdirectories'''
    subdirs = []
    dir_size = 0

    for directory in dirs:
        if isinstance(directory, list):
            subdirs += sum_dir_sizes(directory)
            dir_size += subdirs[-1]
        else:
            dir_size += directory

    return subdirs + [dir_size]


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    sizes = find_dir_sizes(dataset[0]['/'])
    sums = sum_dir_sizes(sizes)

    return sum([size for size in sums if size < 100_000])


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    disk_capacity = 70_000_000
    space_needed = 30_000_000

    sizes = find_dir_sizes(dataset[0]['/'])
    sums = sum_dir_sizes(sizes)

    free_space = disk_capacity - sums[-1]

    candidates = [size for size in sums if free_space + size >= space_needed]

    return min(candidates)
