"""
Module that renders the simulation with pygame.
"""
import pygame
import src.renderer.base as base
import src.engine.grid as gd

class GUIRenderer(base.BaseRenderer):
    """
    Renderer class, using pygame to render the forest fire.
    """
    def __init__(self, grid, update_rate=0.2, number_steps=30):
        super().__init__(grid, update_rate=update_rate, number_steps=number_steps)
        pygame.init()
        self.width = 960
        self.height = 720
        self.cell_width = 960//grid.width
        self.cell_height = 720//grid.height
        self.x_offset = (960 - self.cell_width * grid.width)/2
        self.y_offset = (720 - self.cell_height * grid.height)/2
        self.screen = pygame.display.set_mode((self.width, self.height))

    def render(self):
        step = 1
        while step < self.number_steps and self.update():
            step += 1

    def update(self):
        super().update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.screen.fill((0, 0, 0))
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell = pygame.Rect(self.x_offset + x*self.cell_width, self.y_offset + y*self.cell_height, self.cell_width, self.cell_height)
                if self.grid[x, y] == gd.BURNING:
                    color = 255, 0, 0
                elif self.grid[x, y] == gd.TREE:
                    color = 0, 128, 0
                else:
                    color = 50, 50, 50
                pygame.draw.rect(self.screen, color, cell)
        pygame.display.flip()
        return True
