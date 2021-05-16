import sys
import pygame
from user_events import check_mouse_events
from tile import Tile

def menu(gameloop):
    """menu screen for the game

    Args:
        gameloop ([type]): [description]
    """
    while gameloop.menu:
        gameloop.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]: # pylint: disable=no-member
            sys.exit()

        display = gameloop.display
        display.display.fill((137, 201, 239))
        pygame.draw.rect(display.display, (253,110,170), (0,0,1050,200))
        pygame.draw.rect(display.display, (253,110,170), (0,(1050-200),1050,200))

        for button in gameloop.display.buttons:
            if button.name == "start.jpeg" or button.name == "howtoplay.jpeg":
                button.draw(display.display)
                if check_mouse_events(button):
                    if button.name == "start.jpeg":
                        gameloop.menu = False
                        gameloop.game = True
                        gameloop.harry.reset(gameloop.level)
                        gameloop.level.simon.moving = True
                        gameloop.start()
                    if button.name == "howtoplay.jpeg":
                        gameloop.show_info = True
                        info(gameloop)

        pygame.display.flip()

def info(gameloop):
    """shows the instructions for the game

    Args:
        gameloop ([type]): [description]
    """
    while gameloop.show_info:
        gameloop.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                sys.exit()
        display = gameloop.display
        display.display.fill((137, 201, 239))
        pygame.draw.rect(display.display, (253,110,170), (0,0,1050,200))
        pygame.draw.rect(display.display, (253,110,170), (0,(1050-200),1050,200))
        instr = Tile("info.png", 10, 500)
        instr.scaling(995, 500)
        display.display.blit(instr.image, (instr.rect.x, instr.rect.y))
        for button in gameloop.display.buttons:
            if button.name == "menu.jpeg":
                button.draw(display.display)
                if check_mouse_events(button):
                    gameloop.menu = True
                    menu(gameloop)

        pygame.display.flip()
