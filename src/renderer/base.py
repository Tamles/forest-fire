"""
Abstract renderer. Renderer should extend from the BaseRenderer.
"""
import time
from abc import ABC, abstractmethod

def sleep(interval):
    """
    Wrap the call to time.sleep.
    interval: float, the number of seconds to sleep
    """
    time.sleep(interval) # pragma: no cover

class BaseRenderer(ABC):
    """
    Abstract renderer. Specify the interface of a renderer.
    """
    def __init__(self, grid, update_rate, number_steps):
        self.grid = grid
        self.update_rate = update_rate
        self.number_steps = number_steps

    def render(self):
        """
        Should render the forest.
        """
        step = 1
        while step < self.number_steps and self.update():
            step += 1

    def update(self):
        """
        Should update the current state of the forest.
        """
        self.grid.update()
        sleep(self.update_rate)
