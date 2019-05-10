"""
Module that defines grid object, which contains cells.
"""
import random
from copy import deepcopy

EMPTY = 'empty'
TREE = 'tree'
BURNING = 'burning'

class Grid:
    """
    Grid object.
    Cells can be accessed with grid[x][y] notation.
    """
    def __init__(self, height, width, planting_rate=0, lightning_rate=0):
        self.width = width
        self.height = height
        self.planting_rate = planting_rate
        self.lightning_rate = lightning_rate
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
        """
        Update the state of the forest.
        Spread fire to adjacent trees.
        Burning cell become empty.
        Plant new trees.
        One lightning can strike.
        """
        new_grid = deepcopy(self._grid)
        for y in range(self.height):
            for x in range(self.width):
                if self._neighbor_burning(x, y) and self._grid[y][x] == TREE:
                    new_grid[y][x] = BURNING
                if self._grid[y][x] == BURNING:
                    new_grid[y][x] = EMPTY
                if self._grid[y][x] == EMPTY and random.random() < self.planting_rate:
                    new_grid[y][x] = TREE
        if random.random() < self.lightning_rate:
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            if self._grid[y][x] == TREE:
                new_grid[y][x] = BURNING
        self._grid = new_grid

    def _neighbor_burning(self, x, y):
        """
        Return True if an adjacent cell is burning, False otherwise
        """
        neighbors = self.get_neighbor(x, y)
        for neighbor in neighbors:
            if self[neighbor] == BURNING:
                return True
        return False

    def get_neighbor(self, x, y):
        """
        Return a list of coordinates of neighbors.
        Take into account the edges and corners of the grid.
        """
        x_range = range(x - 1 if x - 1 >= 0 else 0, x + 2 if x + 2 <= self.width else self.width)
        y_range = range(y - 1 if y - 1 >= 0 else 0, y + 2 if y + 2 <= self.height else self.height)
        for i in x_range:
            for j in y_range:
                if (y, x) != (j, i):
                    yield (i, j)
