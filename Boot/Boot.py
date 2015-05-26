import pygame
from Helpers.Artist import *
from Map.TileGrid import *

class Boot:

    artist = Artist()
    artist.begin_session()

    clock = pygame.time.Clock()

    gameExit = False

    grid = TileGrid("ProjectEen.txt")

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        artist.clear_screen()

        grid.draw()
        print(clock.get_fps())
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    Boot()