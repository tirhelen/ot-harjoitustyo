import os
import pygame
from user_events import check_keyboard_events

class Harry(pygame.sprite.Sprite):
    """class for the playable character, Harry
    Args:
        pygame (sprite):
    """
    def __init__(self, map):
        """constructor for Harry

        Args:
            map (map): the map for the playable level
        """
        super().__init__()
        self.reset(map)

    def reset(self,map):
        """resets Harry in starting condition

        Args:
            map (map): the map for the playable level
        """
        dirname = os.path.dirname(__file__)
        self.image = pygame.image.load(os.path.join(dirname, "assets", "Harry.png"))
        self.image = pygame.transform.scale(self.image,(80, 200))
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
        """updates Harry's position
        """
        self.dx = 0 # pylint: disable=invalid-name
        self.dy = 0 # pylint: disable=invalid-name

        check_keyboard_events(self)

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10

        self.dy += self.vel_y
        self.wall_collisions()
        self.object_collisions()
        self.rect.x += self.dx
        self.rect.y += self.dy

    def move_right(self):
        self.dx += 10
    def move_left(self):
        self.dx -= 10
    def jump(self):
        self.vel_y = -20
        self.jumped = True

    def wall_collisions(self):
        """checks if Harry is colliding with any walls

        Args:
            map (Map): the map for the playable level
        """
        for tile in self.map.tiles:
            if tile.name == "platform.jpeg":
                if tile.rect.colliderect(self.rect.x + self.dx,
                                        self.rect.y, self.width, self.height):
                    self.dx = 0
                if tile.rect.colliderect(self.rect.x,
                                        self.rect.y + self.dy, self.width, self.height):
                    if self.vel_y < 0:
                        self.dy = tile.rect.bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        self.dy = tile.rect.top - self.rect.bottom
                        self.vel_y = 0

    def object_collisions(self):
        """checks if Harry is colling with any objects (scarfs or Simon the enemy)

        Args:
            map (Map): the map for the playable level
        """
        self.check_backpack()
        #collides with boas
        for boa in self.map.boa_group:
            # checking if boa collides from right
            if self.rect.x + self.width == boa.rect.x and self.rect.y == boa.rect.y:
                self.backpack.append(boa)
                self.map.boa_group.remove(boa)
            # checking if boa collides from left
            elif self.rect.x == boa.rect.x + boa.image.get_width() and self.rect.y == boa.rect.y:
                self.backpack.append(boa)
                self.map.boa_group.remove(boa)

        #collides with simon
        if self.rect.colliderect(self.map.simon.rect):
            for door in self.map.door_group:
                if door.name == "closeddoor.png":
                    door.rect.x = self.map.door_x
                elif door.name == "opendoor.png":
                    door.rect.x = 1100
            for boa in self.backpack:
                self.map.boa_group.add(boa)
                self.backpack.remove(boa)

    def check_door_collision(self):
        """checks if Harry is colliding with the door

        Args:
            map ([type]): [description]

        Returns:
            Collision (Boolean): true if Harry collides with the door when it's open
        """
        collision = False
        door_collided = pygame.sprite.spritecollide(self, self.map.door_group,
                                                    False, collided = None)
        for door in door_collided:
            if door.name == "opendoor.png":
                collision = True
        return collision

    def check_backpack(self):
        """checks if backpack is "full" and changes the door conditions based on that

        Args:
            map ([type]): [description]
        """
        if len(self.backpack) == 3:
            for door in self.map.door_group:
                if door.name == "closeddoor.png":
                    door.rect.x = 1100
                elif door.name == "opendoor.png":
                    door.rect.x = self.map.door_x
