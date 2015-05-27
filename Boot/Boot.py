import pygame
from Helpers.Artist import *
from Map.TileGrid import *
from GameStateManager.GameStateManager import *

class Boot:

    artist = Artist()
    artist.begin_session()

    clock = pygame.time.Clock()

    gameExit = False

    gsm = GameStateManager()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        artist.clear_screen()

        gsm.update()
        gsm.draw()

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    Boot()