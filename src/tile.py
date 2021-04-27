import os
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, name, X, Y):
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.name = name
        self.image = pygame.image.load(os.path.join(dirname, "assets", self.name))
        self.rect = self.image.get_rect()
        self.rect.x = X # pylint: disable=invalid-name
        self.rect.y = Y # pylint: disable=invalid-name

    def scaling(self, height, width):
        self.image = pygame.transform.scale(self.image, (height, width))
