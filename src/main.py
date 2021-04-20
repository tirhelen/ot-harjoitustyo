import sys
import pygame
from harry import Harry # pylint: disable=import-error
from simon import Simon # pylint: disable=import-error
from level1 import Map # pylint: disable=import-error
from display import Display # pylint: disable=import-error

def main():

    pygame.init() # pylint: disable=no-member
    clock = pygame.time.Clock()
    display = Display(1050,1050,"Harryn huivit häveyksissä")
    pygame.display.set_caption(display.caption)
    level = Map("level1..csv")
    simon = Simon()
    harry = Harry(level, simon, level.boa_group)

    while True:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                sys.exit()

        level.load_tiles()
        harry.update()
        display.display.fill((51, 51, 51))

        for tile in level.tiles:
            display.display.blit(tile.image, (tile.rect.x, tile.rect.y))

        display.display.blit(harry.image, (harry.rect.x, harry.rect.y))
        display.display.blit(simon.image, (simon.rect.x, simon.rect.y))
        level.boa_group.draw(display.display)
        simon.move()
        pygame.display.flip()
if __name__ == "__main__":
    main()
