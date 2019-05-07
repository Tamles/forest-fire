"""
Main module.
"""
import argparse
import src.engine.grid as gd

def main():
    """
    Main function.
    Parse arguments and run the simulator.
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    grid = gd.Grid(4, 5)

    grid[0][3] = 'tree'
    for r in grid:
        print(r)

    for y in range(grid.height):
        for x in range(grid.width):
            print(grid[y][x])
        print()

if __name__ == "__main__":
    main()
