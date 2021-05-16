import os
import pygame


class Simon(pygame.sprite.Sprite):
    """Class for the enemy in the game"""
    def __init__(self):
        """constructor for the enemy, Simon"""
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(dirname, "assets", "Simon.png"))
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = 50
        self.rect.y = 900
        self.direction = 1 # 1 = right, 3 = left
        self.moving = True

    def move(self):
        """moves the enemy"""
        if self.moving:
            if self.direction == 1:
                self.rect.x += 5
                if self.rect.x == 720:
                    self.direction = 3
            elif self.direction == 3:
                self.rect.x -= 5
                if self.rect.x == 20:
                    self.direction = 1
