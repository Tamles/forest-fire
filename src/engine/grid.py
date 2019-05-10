"""
Module that defines grid object, which contains cells.
"""
from copy import deepcopy

EMPTY = 'empty'
TREE = 'tree'
BURNING = 'burning'

class Grid:
    """
    Grid object.
    Cells can be accessed with grid[x][y] notation.
    """
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self._grid = [[EMPTY]*width for _ in range(height)]

    def __getitem__(self, index):
        x, y = index
        return self._grid[y][x]

    def __setitem__(self, index, value):
        x, y = index
        self._grid[y][x] = value

    def __len__(self):
        return self.width * self.height

    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield self._grid[y][x]

    def update(self):
        new_grid = deepcopy(self._grid)
        for y in range(self.height):
            for x in range(self.width):
                if self._neighbor_burning(x, y) and self._grid[y][x] == TREE:
                    new_grid[y][x] = BURNING
                if self._grid[y][x] == BURNING:
                    new_grid[y][x] = EMPTY
        self._grid = new_grid

    def _neighbor_burning(self, x, y):
        neighbors = self.get_neighbor(x, y)
        for ng in neighbors:
            if self[ng] == BURNING:
                return True
        return False

    def get_neighbor(self, x, y):
        x_range = range(x - 1 if x - 1 >= 0 else 0, x + 2 if x + 2 <= self.width else self.width)
        y_range = range(y - 1 if y - 1 >= 0 else 0, y + 2 if y + 2 <= self.height else self.height)
        for i in x_range:
            for j in y_range:
                if (y, x) != (j, i):
                    yield (i, j)
