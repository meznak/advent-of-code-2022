'''A* pathfinding node'''


class Node():
    '''Pathfinding node'''
    def __init__(self, value: int, parent=None, position=None):
        self.value = value
        self.position = position
        self.parent = parent
        self.children = []
        self.visited = False

    def __eq__(self, other) -> bool:
        return self.position == other.position
