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

    @abstractmethod
    def render(self):
        """
        Should render the forest.
        """
        raise NotImplementedError   # pragma: no cover
