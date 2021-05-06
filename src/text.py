import pygame
from display import Display
import sys
class Text:
    def __init__(self, font_and_size: tuple, colour: tuple, text: str, x_y: tuple):
        self.font = pygame.font.SysFont(font_and_size[0], font_and_size[1])
        self.colour = colour
        self.text = self.font.render(text, True, self.colour)
        self.coordinates = x_y
    
    def draw_text(self, display):
        display.blit(self.text, self.coordinates)
    
    def update_text(self, text):
        self.text = self.font.render(text, True, self.colour)