import sys
import pygame
from harry import Harry # pylint: disable=import-error
from level1 import Map # pylint: disable=import-error
from display import Display # pylint: disable=import-error

def main():

    pygame.init() # pylint: disable=no-member
    clock = pygame.time.Clock()
    display = Display(1050,1050,"Harryn huivit häveyksissä")
    pygame.display.set_caption(display.caption)
    level = Map("level1..csv")
    harry = Harry(level)
    level.load_tiles()
    while True:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                sys.exit()

        harry.update()
        display.display.fill((51, 51, 51))

        level.draw_tiles(level.tiles, display.display)

        level.boa_group.draw(display.display)
        level.door_group.draw(display.display)
        display.display.blit(level.simon.image, (level.simon.rect.x, level.simon.rect.y))
        display.display.blit(harry.image, (harry.rect.x, harry.rect.y))
        #level.simon.move()
        pygame.display.flip()

if __name__ == "__main__":
    main()
