import pygame
from button import Button
from user_events import check_mouse_events
from tile import Tile
import sys

def menu(gameloop):
    while gameloop.menu:
        gameloop.clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=no-member
                    sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
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
        instr.scaling(970,500)
        display.display.blit(instr.image, (instr.rect.x, instr.rect.y))
        for button in gameloop.display.buttons:
            if button.name == "menu.jpeg":
                button.draw(display.display)
                if check_mouse_events(button):
                    gameloop.menu = True
                    menu(gameloop)

        pygame.display.flip()