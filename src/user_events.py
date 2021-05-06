import pygame

def check_keyboard_events(harry):
    if not harry.game_over:
        key = pygame.key.get_pressed()
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
