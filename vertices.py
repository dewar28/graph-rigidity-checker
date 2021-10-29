import pygame
from pygame.sprite import Sprite


class Vertex(Sprite):

    def __init__(self, gb_game):
        super().__init__()
        self.screen = gb_game.screen

        self.color = (0, 0, 0)

        self.size = 30

        self.name = 0

        self.rect = pygame.Rect(0, 0, self.size, self.size)



    def draw_vertex(self):
        """Draw the vertex on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
