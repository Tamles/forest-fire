"""
Module to render a forest in the console.
"""

import src.renderer.base as base
import src.engine.grid as gd

class CLIRenderer(base.BaseRenderer):
    """
    CLI Renderer.
    Extend from the base renderer and implement the render method.
    """

    def __init__(self, grid):
        super().__init__(grid)

    def render(self):
        """
        Display a string in the console that represents the state of the forest.
        Each row is separated by a newline.
        Each cell in a row is next to the previous one.
        """
        cells = [cell for cell in self.grid]
        display = "\n".join(["".join(
                                    [self._render_cell(cell) for cell in cells[i * self.grid.width:(i + 1) * self.grid.width]]
                                    ) for i in range(self.grid.height)])
        print(display)

    def update(self):
        pass

    @staticmethod
    def _render_cell(cell):
        """
        Return a character based on the state of the cell.
        """
        cells = {gd.EMPTY: '.', gd.TREE: 'o', gd.BURNING: 'x'}
        return cells[cell]
