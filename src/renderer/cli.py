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
        display = "\n".join("".join([self._render_cell(cell) for cell in row]) for row in self.grid)
        print(display)

    @staticmethod
    def _render_cell(cell):
        """
        Return a character based on the state of the cell.
        """
        cells = {gd.EMPTY: '.', gd.TREE: 'o', gd.BURNING: 'x'}
        return cells[cell]
