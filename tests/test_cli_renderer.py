import random
from pytest_mock import mocker
import src.renderer.cli as cli_renderer
import src.engine.grid as gd

class TestCLIRender:
    def test_display_empty(self, capsys):
        EMPTY_GRID = """.....
.....
.....
.....
"""
        grid = gd.Grid(4, 5)
        renderer = cli_renderer.CLIRenderer(grid)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == EMPTY_GRID

    def test_display_grid_one_tree(self, capsys):
        ONE_TREE_GRID = """..o
...
"""
        grid = gd.Grid(2, 3)
        grid[2, 0] = gd.TREE
        renderer = cli_renderer.CLIRenderer(grid)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == ONE_TREE_GRID

    def test_display_grid_one_burning(self, capsys):
        ONE_BURNING_GRID = """..
.x
..
"""
        grid = gd.Grid(3, 2)
        grid[1, 1] = gd.BURNING
        renderer = cli_renderer.CLIRenderer(grid)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == ONE_BURNING_GRID


    def test_time_update(self, mocker):
        mocker.patch('src.renderer.cli.sleep')
        grid = gd.Grid(3, 2)
        renderer = cli_renderer.CLIRenderer(grid, update_rate=1)
        renderer.update()
        cli_renderer.sleep.assert_called_with(1)

    def test_render(self, mocker, capsys):
        FOREST = """.....
.....
.....

..oo.
o.oo.
..o..

..ooo
o.oo.
.oooo

o.ooo
oooo.
.ooxo

o.xoo
ooxx.
oox.x

o..xx
ox...
ox.o.

xo...
x.o.o
x..o.

.xooo
.oxoo
..oo.
"""
        mocker.patch('src.renderer.cli.sleep')
        grid = gd.Grid(3, 5, 0.5, 0.7)
        random.seed(0)
        renderer = cli_renderer.CLIRenderer(grid, update_rate=1, number_steps=7)
        renderer.render()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == FOREST
