"""
Module that defines grid object, which contains cells.
"""
EMPTY = 'empty'

class Grid:
    """
    Grid object.
    Cells can be accessed with grid[x][y] notation.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._grid = [[EMPTY]*width for _ in range(height)]

    def __getitem__(self, index):
        return self._grid[index]

    def __len__(self):
        return len(self._grid)
