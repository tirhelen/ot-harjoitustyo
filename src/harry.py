import os
import pygame
from user_events import check_keyboard_events

class Harry(pygame.sprite.Sprite):
    def __init__(self, map):
        super().__init__()
        self.reset(map)
    
    def reset(self,map):
        dirname = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(dirname, "assets", "Harry.png"))
        self.image = pygame.transform.scale(self.image, (80, 200))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = 50 # pylint: disable=invalid-name
        self.rect.y = 50 # pylint: disable=invalid-name
        self.vel_y = 0
        self.jumped = False
        self.map = map
        self.backpack = []
        self.game_over = False
    

    def update(self):
        self.dx = 0 # pylint: disable=invalid-name
        self.dy = 0 # pylint: disable=invalid-name

        check_keyboard_events(self)

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        
        self.dy += self.vel_y
        self.wall_collisions(self.map)
        self.object_collisions(self.map)
        self.rect.x += self.dx
        self.rect.y += self.dy

    def move_right(self):
        self.dx += 10
    def move_left(self):
        self.dx -= 10
    def jump(self):
        self.vel_y = -15
        self.jumped = True

    def wall_collisions(self, map):
        for tile in map.tiles:
            if tile.name == "platform.jpeg":
                if tile.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                    self.dx = 0
                if tile.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                    if self.vel_y < 0:
                        self.dy = tile.rect.bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        self.dy = tile.rect.top - self.rect.bottom
                        self.vel_y = 0

    def object_collisions(self, map):
        self.check_backpack(map)
        #collides with boas
        for boa in map.boa_group:
            # checking if boa collides from right
            if self.rect.x + self.width == boa.rect.x and self.rect.y == boa.rect.y:
                   self.backpack.append(boa)
                   map.boa_group.remove(boa)
            # checking if boa collides from left
            elif self.rect.x == boa.rect.x + boa.image.get_width() and self.rect.y == boa.rect.y:
                self.backpack.append(boa)
                map.boa_group.remove(boa)

        #collides with simon
        if self.rect.colliderect(map.simon.rect):
            for door in map.door_group:
                    if door.name == "closeddoor.png":
                        door.rect.x = map.door_x
                    elif door.name == "opendoor.png":
                        door.rect.x = 1100
            for boa in self.backpack:
                    map.boa_group.add(boa)
                    self.backpack.remove(boa)

    def check_door_collision(self, map):
        door_collided = pygame.sprite.spritecollide(self, map.door_group, False, collided = None)
        for door in door_collided:
            if door.name == "opendoor.png":
                return True

    def check_backpack(self, map):
        if len(self.backpack) == 3:
            for door in map.door_group:
                if door.name == "closeddoor.png":
                    door.rect.x = 1100
                elif door.name == "opendoor.png":
                    door.rect.x = map.door_x