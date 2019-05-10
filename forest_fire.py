"""
Main module.
"""
import argparse
import random
import time
import src.engine.grid as gd
import src.renderer.cli as cli_rd

def probability(x):
    x = float(x)
    if x < 0 or x > 1:
        raise argparse.ArgumentTypeError("{} is not a valid probability, should be between 0 and 1".format(x))
    return x

def positive_int(x):
    x = int(x)
    if x < 0:
        raise argparse.ArgumentTypeError("{} is not a positive integer, should be 0 or higher".format(x))
    return x

def positive_float(x):
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
    parser.add_argument('--number_steps', type=positive_int, help="Number of steps before the simulation ends", default=10)
    parser.add_argument('--planting_rate', type=probability, help="Probability of a tree to grow on an empty cell", default=0.1)
    parser.add_argument('--lightning_rate', type=probability, help="Probability of a light to strike each step", default=0.1)
    args = parser.parse_args()
    update_rate = args.update_rate
    number_steps = args.number_steps
    planting_rate = args.planting_rate
    lightning_rate = args.lightning_rate
    grid = gd.Grid(13, 13, planting_rate=planting_rate, lightning_rate=lightning_rate)
    renderer = cli_rd.CLIRenderer(grid, update_rate=update_rate, number_steps=number_steps)
    renderer.render()

if __name__ == "__main__":
    main()
