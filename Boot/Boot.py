import pygame
from Helpers.Artist import *
from LevelStateManager.LevelStateManager import *

class Boot(object):

    def __init__(self):
        # Make a window with the specified window dimensions and caption.
        Artist.begin_session()

        game_exit = False

        clock = pygame.time.Clock()

        lsm = LevelStateManager()

        lsm.run()

        while not game_exit:
            # Event handling:
            # Pygame removes all events from the queue.
            # pygame.quit argument ensures that only the pygame.quit events are removed.
            for event in pygame.event.get(pygame.QUIT):
                game_exit = True

            # Clear the screen with a black
            Artist.clear_screen()

            lsm.update()
            lsm.draw()

            # Render all objects.
            pygame.display.update()

            # Set the frames per seconds.
            clock.tick(60)

        pygame.quit()
        quit()

if __name__ == '__main__':
    Boot().__init__()


