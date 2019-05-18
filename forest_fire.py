"""
Main module.
"""
import argparse
import src.engine.grid as gd
import src.renderer.cli as cli_rd
import src.renderer.pygame as gui_rd
import src.renderer.debug as debug_rd

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
    parser.add_argument('--planting_rate', type=probability, help="Probability of a tree to grow on an empty cell", default=0.01)
    parser.add_argument('--lightning_rate', type=probability, help="Probability of a light to strike each step", default=0.4)
    parser.add_argument('-W', '--width', type=positive_int, help="Width of the forest", default=24)
    parser.add_argument('-H', '--height', type=positive_int, help="Height of the forest", default=18)
    parser.add_argument('--renderer', help="Which renderer to use", default='cli')
    parser.add_argument('--no_initial_state', help="Pregenerate forest", action='store_true')
    args = parser.parse_args()
    update_rate = args.update_rate
    number_steps = args.number_steps
    planting_rate = args.planting_rate
    lightning_rate = args.lightning_rate
    width = args.width
    height = args.height
    initial_state = not args.no_initial_state
    grid = gd.Grid(height, width, planting_rate=planting_rate, lightning_rate=lightning_rate, initial_state=initial_state)
    if args.renderer == 'gui':
        renderer = gui_rd.GUIRenderer(grid, update_rate=update_rate, number_steps=number_steps)
    elif args.renderer == 'cli':
        renderer = cli_rd.CLIRenderer(grid, update_rate=update_rate, number_steps=number_steps)
    elif args.renderer == 'debug':
        renderer = debug_rd.DebugRenderer(grid, update_rate=update_rate, number_steps=number_steps)
    renderer.render()

if __name__ == "__main__":
    main()
