import pygame
from button import Button

class Display():
    def __init__(self, height, width, caption):
        self.height = height
        self.width = width
        self.display = pygame.display.set_mode((self.width, self.height))
        self.caption = caption
        self.buttons = [Button("restart.jpeg", 250, 250), Button("menu.jpeg", 250, 400), Button("start.jpeg", 400, 250), Button("howtoplay.jpeg", 400, 400)]
