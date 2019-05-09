import sys
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

    def test_update_grid_new_tree(self):
        grid = gd.Grid(4, 5)
        for y in range(grid.height):
            for x in range(grid.width):
                assert grid[y][x] == gd.EMPTY

        grid.update()
        #assert grid[0][0] == gd.TREE

    def test_get_neightboor_corner_0_0(self):
        grid = gd.Grid(4, 5)
        neightboor = [cell for cell in grid.get_neightboor(0, 0)]
        assert neightboor == [(0, 0), (1, 0), (0, 1), (1, 1)]

    def test_get_neightboor_corner_0_w(self):
        grid = gd.Grid(4, 5)
        neightboor = [cell for cell in grid.get_neightboor(0, grid.width - 1)]
        assert neightboor == [(0, 3), (1, 3), (0, 4), (1, 4)]

    def test_get_neightboor_corner_h_w(self):
        grid = gd.Grid(4, 5)
        neightboor = [cell for cell in grid.get_neightboor(grid.height - 1, grid.width - 1)]
        assert neightboor == [(2, 3), (3, 3), (2, 4), (3, 4)]

    def test_get_neightboor_corner_h_0(self):
        grid = gd.Grid(4, 5)
        neightboor = [cell for cell in grid.get_neightboor(grid.height - 1, 0)]
        assert neightboor == [(2, 0), (3, 0), (2, 1), (3, 1)]

    def test_get_neightboor_edge_vert(self):
        grid = gd.Grid(4, 5)
        neightboor = [cell for cell in grid.get_neightboor(2, 0)]
        assert neightboor == [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1)]
