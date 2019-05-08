import src.renderer.cli as cli_renderer
import src.engine.grid as gd

class TestCLIRender:
    def test_render_empty(self):
        EMPTY_GRID = """.....
.....
.....
....."""
        grid = gd.Grid(4, 5)
        renderer = cli_renderer.CLIRenderer(grid)
        assert renderer.render() == EMPTY_GRID
