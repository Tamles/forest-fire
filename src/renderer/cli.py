import src.renderer.base as base
import src.engine.grid as gd

class CLIRenderer(base.BaseRenderer):
    def __init__(self, grid):
        super().__init__(grid)

    def render(self):
        display = ""
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                display += self._render_cell(self.grid[y][x])
            display += "\n"
        return display[:~0]

    def _render_cell(self, cell):
        CELLS = {gd.EMPTY: '.', gd.TREE: 'o', gd.BURNING: 'x'}
        return CELLS[cell]
