import os
import pygame

class Harry(pygame.sprite.Sprite):
    def __init__(self, map, simon, boa_group):
        super().__init__()
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
        self.simon = simon
        self.boa_group = boa_group
        self.found = 0

    def update(self):
        self.dx = 0 # pylint: disable=invalid-name
        self.dy = 0 # pylint: disable=invalid-name
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # pylint: disable=no-member
            self.dx -= 10
        if key[pygame.K_RIGHT]: # pylint: disable=no-member
            self.dx += 10
        if key[pygame.K_SPACE] and self.jumped is False: # pylint: disable=no-member
            self.jumped = True
            self.vel_y = -15
        if key[pygame.K_SPACE] is False: # pylint: disable=no-member
            self.jumped = False

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y
        self.collisions(self.map, self.simon, self.boa_group)
        self.rect.x += self.dx
        self.rect.y += self.dy

    def collisions(self, map, simon, group):
        for tile in map.tiles:
            if tile.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            if tile.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if self.vel_y < 0:
                    self.dy = tile.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    self.dy = tile.rect.top - self.rect.bottom
                    self.vel_y = 0
        if self.rect.colliderect(simon.rect):
            print("rip")
        if pygame.sprite.spritecollide(self, group, False):
            self.found += 1
            print(self.found)
            print("huivi")
