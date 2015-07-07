import pygame
from Helpers.Artist import *
from LevelStateManager.LevelStateManager import *

class Boot(object):

    def __init__(self):
        # This statement calls the static method begin_session in the artist class.
        # This method makes a window with the specified
        Artist.begin_session()

        game_exit = False

        # Creates a new clock object. This class can be found in the pygame library.
        # This object can be used to track an amount of time.
        # The clock also provides functions to control the framerate.
        clock = pygame.time.Clock()

        # Make a new LevelStateManager object. The level state manager is used to switch between the levels.
        lsm = LevelStateManager()

        lsm.run()

        while not game_exit:
            # Event handling:
            # Pygame removes all events from the queue.
            # Pygame.quit argument ensures that only the pygame.quit events are removed.
            for event in pygame.event.get(pygame.QUIT):
                game_exit = True

            # Calls the update and draw method of the current level.
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


