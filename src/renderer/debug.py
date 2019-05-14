"""
Module to render a forest in the console.
"""
from colorama import Back, Fore, init
import src.renderer.base as base
import src.engine.grid as gd

class DebugRenderer(base.BaseRenderer):
    """
    CLI Renderer.
    Extend from the base renderer and implement the render method.
    """

    def __init__(self, grid, update_rate=0.2, number_steps=10):
        """
        grid: grid object, the grid which will be rendered
        update_rate: float, the time between two steps
        number_steps: int, the number of steps the simulation will run
        """
        init()
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
        """
        Update the forest and display it, and sleep until next step.
        """
        super().update()

    def render(self):
        """
        Simulate the forest fire.
        """
        step = 1
        self.display()
        while step < self.number_steps:
            self.update()
            self.display()
            step += 1

    @staticmethod
    def _color_text(text, color):
        """
        Add ANSI code to text to change the color of the text.
        text: string, the text which should be colorized
        color: string, color name that is available in colorama
        """
        return Fore.__dict__[color] + Back.__dict__[color] + text + Back.RESET + Fore.RESET

    @staticmethod
    def _render_cell(cell):
        """
        Return a character based on the state of the cell.
        cell: string, one of the 3 states available in the grid: EMPTY, TREE or BURNING
        """
        return str(cell)
