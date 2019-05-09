"""
Abstract renderer. Renderer should extend from the BaseRenderer.
"""
from abc import ABC, abstractmethod

class BaseRenderer(ABC):
    """
    Abstract renderer. Specify the interface of a renderer.
    """
    def __init__(self, grid):
        self.grid = grid

    @abstractmethod # pragma: no mutate
    def render(self):
        """
        Should render the forest.
        """
        raise NotImplementedError   # pragma: no cover

    @abstractmethod # pragma: no mutate
    def update(self):
        """
        Should update the current state of the forest.
        """
        raise NotImplementedError   # pragma: no cover
