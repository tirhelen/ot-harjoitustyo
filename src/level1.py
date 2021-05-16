import os
import csv
import pygame
from simon import Simon # pylint: disable=import-error
from tile import Tile # pylint: disable=import-error

class Map:
    """class for level / map"""
    def __init__(self, filename):
        """constructor for the map

        Args:
            filename (string): name of the csv file that has information about the map tiles
        """
        self.filename = filename
        self.tile_size = 50
        self.start_x, self.start_y = 0,0
        self.boa_group = pygame.sprite.Group()
        self.simon = Simon()
        self.door_group = pygame.sprite.Group()

    def draw_tiles(self, tile_list, screen):
        """draws tiles in the screen

        Args:
            tile_list (list): list of the tiles created in load_tiles
            screen (display): the display in which the tiles will be drawn
        """
        for tile in tile_list:
            screen.blit(tile.image, (tile.rect.x, tile.rect.y))

    def read_csv(self):
        """reads the csv file and creates list of tile numbers

        Returns:
            map [list]: list of tile numbers
        """
        map = []
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, "assets", self.filename)) as data:
            data = csv.reader(data, delimiter=",")
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self):
        """creates list of tiles based on their tile number in map list"""
        self.tiles = []
        map = self.read_csv()
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == "0":
                    platform_tile = Tile("platform.jpeg", j*self.tile_size, i*self.tile_size)
                    self.tiles.append(platform_tile)
                elif map[i][j] == "1":
                    scarf = Tile("Boa1.png", j*self.tile_size, i*self.tile_size)
                    scarf.scaling(80, 200)
                    self.boa_group.add(scarf)
                elif map[i][j] == "2":
                    scarf = Tile("Boa2.png", j*self.tile_size, i*self.tile_size)
                    scarf.scaling(80, 200)
                    self.boa_group.add(scarf)
                elif map[i][j] == "3":
                    scarf = Tile("Boa3.png", j*self.tile_size, i*self.tile_size)
                    scarf.scaling(80, 200)
                    self.boa_group.add(scarf)
                elif map[i][j] == "4":
                    self.door_x = j*self.tile_size
                    self.door1 = Tile("closeddoor.png", j*self.tile_size, i*self.tile_size)
                    self.door1.scaling(80, 200)
                    self.door_group.add(self.door1)
                    self.door2 = Tile("opendoor.png", j*self.tile_size+200, i*self.tile_size)
                    self.door2.scaling(80, 200)
                    self.door_group.add(self.door2)
