"""
Main module.
"""
import argparse
import random
import time
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
            if random.random() > 0.4:
                grid[x, y] = gd.TREE

    renderer = cli_rd.CLIRenderer(grid)
    renderer.render()
    print()
    grid[6, 0] = 'burning'
    renderer.render()
    while gd.BURNING in grid:
        time.sleep(0.2)
        grid.update()
        print()
        renderer.render()

if __name__ == "__main__":
    main()
