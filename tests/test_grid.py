import src.engine.grid as gd

class TestGrid:
    def test_constants(self):
        assert gd.EMPTY == 'empty'
        assert gd.TREE == 'tree'
        assert gd.BURNING == 'burning'

    def test_empty_grid(self):
        grid = gd.Grid(4, 5)
        for y in range(grid.height):
            for x in range(grid.width):
                assert grid[y][x] == gd.EMPTY

    def test_len_grid(self):
        grid = gd.Grid(4, 5)
        assert len(grid) == 4 * 5
