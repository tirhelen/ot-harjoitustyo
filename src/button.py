import os
import pygame
class Button(pygame.sprite.Sprite):
    """class for buttons

    Args:
        pygame (sprite):
    """
    def __init__(self, name, X, Y):
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.name = name
        self.image = pygame.image.load(os.path.join(dirname, "assets", self.name))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.clicked = False

    def draw(self, display):
        display.blit(self.image, self.rect)

