import pygame
import sys
def check_keyboard_events(harry):
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        sys.exit()
    if not harry.game_over:
        if key[pygame.K_LEFT]: # pylint: disable=no-member
            harry.move_left()
        if key[pygame.K_RIGHT]: # pylint: disable=no-member
            harry.move_right()
        if key[pygame.K_SPACE] and not harry.jumped: # pylint: disable=no-member
            harry.jump()
        if not key[pygame.K_SPACE]: # pylint: disable=no-member
            harry.jumped = False
        if key[pygame.K_UP]: # pylint: disable=no-member
            if harry.check_door_collision(harry.map):
                harry.game_over = True

def check_mouse_events(button):
    action = False
    mouse_pos = pygame.mouse.get_pos()
    if button.rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0] == 1 and button.clicked == False:
            action = True
            button.clicked = True
    if pygame.mouse.get_pressed()[0] == 0:
        button.clicked = False
    return action