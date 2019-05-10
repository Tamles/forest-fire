"""
Abstract renderer. Renderer should extend from the BaseRenderer.
"""
from abc import ABC, abstractmethod

class BaseRenderer(ABC):
    """
    Abstract renderer. Specify the interface of a renderer.
    """
    def __init__(self, grid, update_rate, number_steps):
        self.grid = grid
        self.update_rate = update_rate
        self.number_steps = number_steps

    @abstractmethod # pragma: no mutate
    def render(self):
        """
        Should render the forest.
        """
        raise NotImplementedError   # pragma: no cover

    def update(self):
        """
        Should update the current state of the forest.
        """
        self.grid.update()
