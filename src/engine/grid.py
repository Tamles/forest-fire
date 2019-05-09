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
        return self._grid[index]

    def __len__(self):
        return self.width * self.height

    def update(self):
        prev_grid = deepcopy(self._grid)
        for y in range(self.height):
            for x in range(self.width):
                if self._neightboor_burning(y, x) and prev_grid[y][x] == TREE:
                    self._grid[y][x] = BURNING

    def _neightboor_burning(self, y, x):
        pass

    def get_neightboor(self, y, x):
        x_range = range(x - 1 if x - 1 >= 0 else 0, x + 2 if x + 2 <= self.width else self.width)
        y_range = range(y - 1 if y - 1 >= 0 else 0, y + 2 if y + 2 <= self.height else self.height)
        for i in x_range:
            for j in y_range:
                yield (j, i)
