"""
Module to render a forest in the console.
"""
import time
import src.renderer.base as base
import src.engine.grid as gd

def sleep(interval):
    """
    Wrap the call to time.sleep
    """
    time.sleep(interval) # pragma: no cover

class CLIRenderer(base.BaseRenderer):
    """
    CLI Renderer.
    Extend from the base renderer and implement the render method.
    """

    def __init__(self, grid, update_rate=0.2, number_steps=30):
        super().__init__(grid, update_rate, number_steps)

    def display(self):
        """
        Display a string in the console that represents the state of the forest.
        Each row is separated by a newline.
        Each cell in a row is next to the previous one.
        """
        cells = [cell for cell in self.grid]
        output = "\n".join(
            ["".join(
                [self._render_cell(c) for c in cells[i * self.grid.width:(i + 1) * self.grid.width]]
            ) for i in range(self.grid.height)]
        )
        print(output)
        print()

    def update(self):
        super().update()
        sleep(self.update_rate)

    def render(self):
        step = 0
        self.display()
        while step < self.number_steps:
            self.update()
            self.display()
            step += 1

    @staticmethod
    def _render_cell(cell):
        """
        Return a character based on the state of the cell.
        """
        cells = {gd.EMPTY: '.', gd.TREE: 'o', gd.BURNING: 'x'}
        return cells[cell]
