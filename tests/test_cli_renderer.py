import src.renderer.cli as cli_renderer
import src.engine.grid as gd

class TestCLIRender:
    def test_render_empty(self, capsys):
        EMPTY_GRID = """.....
.....
.....
....."""
        grid = gd.Grid(4, 5)
        renderer = cli_renderer.CLIRenderer(grid)
        renderer.render()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == EMPTY_GRID

    def test_render_grid_one_tree(self, capsys):
        ONE_TREE_GRID = """..o
..."""
        grid = gd.Grid(2, 3)
        grid[2, 0] = gd.TREE
        renderer = cli_renderer.CLIRenderer(grid)
        renderer.render()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == ONE_TREE_GRID

    def test_render_grid_one_burning(self, capsys):
        ONE_BURNING_GRID = """..
.x
.."""
        grid = gd.Grid(3, 2)
        grid[1, 1] = gd.BURNING
        renderer = cli_renderer.CLIRenderer(grid)
        renderer.render()
        captured = capsys.readouterr()
        output = captured.out[:~0] # Remove trailing newline
        assert output == ONE_BURNING_GRID
