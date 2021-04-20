import os
import pygame


class Simon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        dirname = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(dirname, "assets", "Simon.png"))
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = 50  # pylint: disable=invalid-name
        self.rect.y = 900 # pylint: disable=invalid-name
        self.direction = 1
        # 1 = right, 3 = left

    def move(self):
        if self.direction == 1:
            self.rect.x += 5
            if self.rect.x == 850:
                self.direction = 3
        elif self.direction == 3:
            self.rect.x -= 5
            if self.rect.x == 20:
                self.direction = 1
