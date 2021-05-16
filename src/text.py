import pygame
from display import Display
class Text:
    """class for text that needs to be shown on the screen"""
    def __init__(self, font_and_size: tuple, colour: tuple, text: str, x_y: tuple):
        """constructor for texts
        Args:
            font_and_size (tuple): font and size of the text
            colour (tuple): colour of the text
            text (str): the actual text
            x_y (tuple): the coordinates where the text will be shown
        """
        self.font = pygame.font.SysFont(font_and_size[0], font_and_size[1])
        self.colour = colour
        self.text = self.font.render(text, True, self.colour)
        self.coordinates = x_y
    
    def draw_text(self, display):
        """draws the text on given display

        Args:
            display (display): the display in which the text will be shown
        """
        display.blit(self.text, self.coordinates)
    
    def update_text(self, text):
        """updates the text if needed
        Args:
            text (str): new text
        """
        self.text = self.font.render(text, True, self.colour)