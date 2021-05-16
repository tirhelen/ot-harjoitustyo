import sys
import pygame
from text import Text
from user_events import check_mouse_events
from menu import menu
class Gameloop:
    """class for the gameloop
    """
    def __init__(self, display, level, harry, clock):
        """constructor for the gameloop

        Args:
            display ([type]): [description]
            level ([type]): [description]
            harry ([type]): [description]
            clock ([type]): [description]
        """
        self.display = display
        self.level = level
        self.harry = harry
        self.clock = clock
        self.game = True
        self.menu = True
        self.show_info = False

    def start(self):
        """starts the game and keeps it going
        """
        self.level.load_tiles()

        while self.game:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=no-member
                    sys.exit()

            self.harry.update()

            score = str(len(self.harry.backpack))
            score_str = "Löydetty " + score + "/3 huivia"
            score_text = Text(("Ariel",50), (0,0,0), score_str, (50,5))

            self.display.display.fill((137, 201, 239))
            self.level.draw_tiles(self.level.tiles, self.display.display)
            self.level.boa_group.draw(self.display.display)
            self.level.door_group.draw(self.display.display)

            score_text.draw_text(self.display.display)

            self.display.display.blit(self.level.simon.image,
                                    (self.level.simon.rect.x, self.level.simon.rect.y))
            self.display.display.blit(self.harry.image, (self.harry.rect.x, self.harry.rect.y))
            self.level.simon.move()

            if self.harry.game_over:
                self.level.simon.moving = False
                for button in self.display.buttons:
                    if button.name == "restart.jpeg" or button.name == "menu.jpeg":
                        button.draw(self.display.display)
                    if check_mouse_events(button):
                        if button.name == "restart.jpeg":
                            self.harry.reset(self.level)
                            self.level.simon.moving = True
                            self.start()
                        elif button.name == "menu.jpeg":
                            self.game = False
                            self.menu = True
                            menu(self)
            pygame.display.flip()
