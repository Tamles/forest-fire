# forest-fire

## Simulation of a forest fire

This project simulates a forest fire based on simple rules.

## Rules

The forest is represented as a grid of cells which can be in defined states:

- empty: the cell is empty, there is no tree and the fire can't propagate through it.

- tree: the cell contains a tree. The tree will burn if a adjacent cell is containing a burning tree.

- burning: the cell contains a burning tree. The fire propagates to the adjacent cells.

## Install

To install the simulator, clone the repo and create a virtual environnement thanks to python-venv.
The version 3.7 of python is required.

Then, in the virtual environnement, run:

```console
(venv) $ pip install -e .
```

## Usage

To run the simulation, run the script:

```console
(venv) $ python forest-fire.py
```
