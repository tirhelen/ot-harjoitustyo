import pygame
from button import Button

class Display():
    def __init__(self, height, width, caption):
        self.height = height
        self.width = width
        self.display = pygame.display.set_mode((self.width, self.height))
        self.caption = caption
        self.buttons = []
        self.create_buttons()
    
    def create_buttons(self):
        restart_button = Button(250, 250, "restart.jpeg")
        menu_button = Button(250, 350, "menu.jpeg")
        self.buttons.append(restart_button)
        self.buttons.append(menu_button)