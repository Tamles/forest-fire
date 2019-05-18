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

    def test_all_ash_phase(self, capsys):
        START = """-1-1-1-1-1
-1-1-1-1-1
-1-15-1-1
-1-1-1-1-1
-1-1-1-1-1
"""
        STEP_1 = """-1-1-1-1-1
-1555-1
-1545-1
-1555-1
-1-1-1-1-1
"""
        STEP_2 = """55555
54445
54345
54445
55555
"""
        STEP_3 = """44444
43334
43234
43334
44444
"""
        STEP_4 = """33333
32223
32123
32223
33333
"""
        STEP_5 = """22222
21112
21012
21112
22222
"""
        STEP_6 = """11111
10001
10001
10001
11111
"""
        grid = gd.Grid(5, 5, planting_rate=0, lightning_rate=0)
        for x in range(grid.width):
            for y in range(grid.height):
                grid[x, y] = gd.TREE
        grid[2, 2] = gd.BURNING
        renderer = debug_rd.DebugRenderer(grid, update_rate=0)
        renderer.display()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == START
        renderer.update()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == STEP_1
        renderer.update()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == STEP_2
        renderer.update()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == STEP_3
        renderer.update()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == STEP_4
        renderer.update()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == STEP_5
        renderer.update()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == STEP_6


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
        renderer = debug_rd.DebugRenderer(grid, number_steps=7)
        renderer.render()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == FOREST
