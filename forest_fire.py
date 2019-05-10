"""
Main module.
"""
import argparse
import src.engine.grid as gd
import src.renderer.cli as cli_rd

def main():
    """
    Main function.
    Parse arguments and run the simulator.
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    grid = gd.Grid(13, 13)
    for x in range(grid.width):
        for y in range(grid.height):
            grid[x, y] = gd.TREE

    renderer = cli_rd.CLIRenderer(grid)
    renderer.render()
    print()
    grid[6, 6] = 'burning'
    renderer.render()
    grid.update()
    print()
    renderer.render()
    grid.update()
    print()
    renderer.render()
    grid.update()
    print()
    renderer.render()
    grid.update()
    print()
    renderer.render()
    grid.update()
    print()
    renderer.render()
    grid.update()
    print()
    renderer.render()
    grid.update()
    print()
    renderer.render()

if __name__ == "__main__":
    main()
