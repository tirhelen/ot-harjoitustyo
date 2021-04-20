import pygame

class Display():
    def __init__(self, height, width, caption):
        self.height = height
        self.width = width
        self.display = pygame.display.set_mode((self.width, self.height))
        self.caption = caption
        