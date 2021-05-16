import os
import pygame
class Button(pygame.sprite.Sprite):
    """class for buttons"""
    def __init__(self, name, X, Y):
        """constructor for buttons

        Args:
            name (string): name of the file that has the button image
            X (int): x coordinate for button placement
            Y (int): y coordinate for button placement
        """
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.name = name
        self.image = pygame.image.load(os.path.join(dirname, "assets", self.name))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.clicked = False

    def draw(self, display):
        """draws the button in given display
        Args:
            display
        """
        display.blit(self.image, self.rect)

