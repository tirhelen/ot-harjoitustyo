import pygame
import os


class Harry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(dirname, "assets", "Harry.png"))
        self.image = pygame.transform.scale(self.image, (80,200))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 0
        self.y = 0
        self.right = False
        self.left = False

    def move_right(self):
            self.x += 5
    def move_left(self):
            self.x -= 5