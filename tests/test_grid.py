import src.engine.grid as gd

class TestGrid:
    def test_empty_grid(self):
        grid = gd.Grid(4, 4)
        for x in range(grid.width):
            for y in range(grid.height):
                assert grid[x][y] == gd.EMPTY
