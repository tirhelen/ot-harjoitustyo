import sys
import pygame
from harry import Harry
from level1 import Map
from display import Display
from button import Button
from text import Text

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

        score = str(len(harry.backpack))
        score_str = "Löydetty " + score + "/3 huivia"
        score_text = Text(("Ariel",50), (0,0,0), score_str, (50,5))

        display.display.fill((51, 51, 51))
        level.draw_tiles(level.tiles, display.display)
        level.boa_group.draw(display.display)
        level.door_group.draw(display.display)
        score_text.draw_text(display.display)
        display.display.blit(level.simon.image, (level.simon.rect.x, level.simon.rect.y))
        display.display.blit(harry.image, (harry.rect.x, harry.rect.y))
        level.simon.move()
        
        if harry.game_over:
            level.simon.moving = False
            display.create_buttons()
            for button in display.buttons:
                button.draw(display.display)

        pygame.display.flip()

if __name__ == "__main__":
    main()