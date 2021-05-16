import pygame
from harry import Harry
from level1 import Map
from display import Display
from gameloop import Gameloop
from menu import menu

def main():
    """creates initializes the program"""
    pygame.init() # pylint: disable=no-member
    clock = pygame.time.Clock()
    display = Display(1050,1050,"Harryn huivit häveyksissä")
    pygame.display.set_caption(display.caption)
    level = Map("level1..csv")
    harry = Harry(level)
    gameloop = Gameloop(display, level, harry, clock)
    menu(gameloop)

main()
