import random
from pytest_mock import mocker
import src.renderer.debug as debug_rd
import src.renderer.base
import src.engine.grid as gd

class TestDebugRender:
    def test_display_empty(self, capsys):
        EMPTY_GRID = """00000
00000
00000
00000
"""
        grid = gd.Grid(4, 5)
        renderer = debug_rd.DebugRenderer(grid)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == EMPTY_GRID

    def test_display_grid_one_tree(self, capsys):
        ONE_TREE_GRID = """00-1
000
"""
        grid = gd.Grid(2, 3)
        grid[2, 0] = gd.TREE
        renderer = debug_rd.DebugRenderer(grid)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == ONE_TREE_GRID

    def test_display_grid_one_burning(self, capsys):
        ONE_BURNING_GRID = """00
05
00
"""
        grid = gd.Grid(3, 2)
        grid[1, 1] = gd.BURNING
        renderer = debug_rd.DebugRenderer(grid)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == ONE_BURNING_GRID


    def test_time_update(self, mocker):
        mocker.patch('src.renderer.base.sleep')
        grid = gd.Grid(3, 2)
        renderer = debug_rd.DebugRenderer(grid)
        renderer.update()
        src.renderer.base.sleep.assert_called_with(0.2)

    def test_render(self, mocker, capsys):
        FOREST = """00-1-10
-10-1-10
00-100

00-1-1-1
-10-1-10
0-1-1-1-1

-10-1-1-1
-1-1-1-10
0-1-15-1

-10-1-1-1
-1-1550
-1-1545

-10555
-1544-1
-15434

50444
54335
54323
"""
        mocker.patch('src.renderer.base.sleep')
        grid = gd.Grid(3, 5, 0.5, 0.7)
        random.seed(0)
        renderer = debug_rd.DebugRenderer(grid, update_rate=1, number_steps=7)
        renderer.render()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == FOREST
