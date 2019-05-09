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
    grid = gd.Grid(4, 5)

    renderer = cli_rd.CLIRenderer(grid)
    renderer.render()
    print()
    grid[0][3] = 'tree'
    renderer.render()

    ng = [cell for cell in grid.get_neighbor(1, 0)]
    print(ng)

if __name__ == "__main__":
    main()
