"""
Main module.
"""
import argparse
import src.engine.grid as gd
import src.renderer.cli as cli_rd

def probability(x):
    """
    Ensure x is a float between 0 and 1.
    """
    x = float(x)
    if x < 0 or x > 1:
        raise argparse.ArgumentTypeError("{} is not a valid probability, should be between 0 and 1".format(x))
    return x

def positive_int(x):
    """
    Ensure x is a positive integer.
    """
    x = int(x)
    if x < 0:
        raise argparse.ArgumentTypeError("{} is not a positive integer, should be 0 or higher".format(x))
    return x

def positive_float(x):
    """
    Ensure x is a positive float.
    """
    x = float(x)
    if x < 0:
        raise argparse.ArgumentTypeError("{} is not a positive float, should be 0.0 or higher".format(x))
    return x

def main():
    """
    Main function.
    Parse arguments and run the simulator.
    """
    parser = argparse.ArgumentParser(description="Run a simulation of forest fire")
    parser.add_argument('--update_rate', type=positive_float, help="Time between two update of the forest, in seconds", default=0.2)
    parser.add_argument('--number_steps', type=positive_int, help="Number of steps before the simulation ends", default=50)
    parser.add_argument('--planting_rate', type=probability, help="Probability of a tree to grow on an empty cell", default=0.1)
    parser.add_argument('--lightning_rate', type=probability, help="Probability of a light to strike each step", default=0.4)
    parser.add_argument('--width', type=positive_int, help="Width of the forest", default=130)
    parser.add_argument('--height', type=positive_int, help="Height of the forest", default=13)
    args = parser.parse_args()
    update_rate = args.update_rate
    number_steps = args.number_steps
    planting_rate = args.planting_rate
    lightning_rate = args.lightning_rate
    width = args.width
    height = args.height
    grid = gd.Grid(height, width, planting_rate=planting_rate, lightning_rate=lightning_rate)
    renderer = cli_rd.CLIRenderer(grid, update_rate=update_rate, number_steps=number_steps)
    renderer.render()

if __name__ == "__main__":
    main()
