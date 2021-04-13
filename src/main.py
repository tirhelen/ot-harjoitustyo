import pygame
import os
from harry import Harry

def main():
    pygame.init()

    display_height = 1000
    display_width = 1000
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Harryn huivit hävöksissä")
    harry = Harry
    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    harry.right = True
                if event.key == pygame.K_LEFT:
                    harry.left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    harry.right = False
                if event.key == pygame.K_LEFT:
                    harry.left = False
            if event.type == pygame.QUIT:
                exit()

        if harry.right:
            harry.move_right()
        if harry.left:
            harry.move_left()
        
        if harry.x < 0:
            harry.x = 0
        if harry.x > (display_width-harry.width):
            harry.x = display_width-harry.width
        if harry.y > (display_height-harry.height):
            harry.y = display_height-harry.height
        if harry.y < 0:
            harry.y = 0
        
        display.fill((0,0,0))
        display.blit(harry.image, (harry.x,harry.y))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
