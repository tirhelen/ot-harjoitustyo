import os
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, X, Y):
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(dirname, "assets", image))
        self.rect = self.image.get_rect()
        self.rect.x = X # pylint: disable=invalid-name
        self.rect.y = Y # pylint: disable=invalid-name

    def scaling(self, height, width):
        self.image = pygame.transform.scale(self.image, (height, width))