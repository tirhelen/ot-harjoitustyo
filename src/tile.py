import os
import pygame

class Tile(pygame.sprite.Sprite):
    """class for tiles used in a map"""
    def __init__(self, name, X, Y):
        """constructor for a tile
        Args:
            name (string): name of the tile image file
            X (int): x coordinate where the tile will place in the map
            Y (int): y coordinate -//-
        """
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.name = name
        self.image = pygame.image.load(os.path.join(dirname, "assets", self.name))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

    def scaling(self, width, height):
        """scales the tile into wanted size
        Args:
            width (int): new width of the tile
            height (int): new height of the tile
        """
        self.image = pygame.transform.scale(self.image, (width, height))
