import pygame
from Helpers.Artist import *
from LevelStateManager.LevelStateManager import *
from Helpers.DatabaseReceiver import *

# Author: Richard Jongenburger.


class Boot(object):

    def __init__(self):
        # This statement calls
        # the static method begin_session in the artist class.
        # This method makes a window.
        Artist.begin_session()

        # Variable to determine when to exit the main game loop.
        game_exit = False

        # Creates a new clock object.
        # This class can be found in the pygame library.
        # This object can be used to track an amount of time.
        # The clock also provides functions to control the framerate.
        clock = pygame.time.Clock()

        # Make a new LevelStateManager object.
        # The level state manager is used to switch between the levels.
        # The LevelStateManager starts with the Main Menu state.
        lsm = LevelStateManager()

        while not game_exit:
            # Event handling:
            # With pygame.event.get(), you get all of the mouse/keyboard
            # input events in pygame's event queue.
            # Those events are automatically removed from the queue,
            # when you call pyagme.event.get() method.
            # The pygame.quit argument ensures that only the
            # pygame.quit events are removed.
            # The pygame.QUIT event means that you close the
            # game window by clicking on the red cross.
            # So when there is a quit event. Exit the game loop.
            for event in pygame.event.get(pygame.QUIT):
                game_exit = True

            # Calls the update and draw method of the current level.
            lsm.update()
            lsm.draw()

            # Render all objects of the game.
            pygame.display.update()

            # Set the frames per seconds.
            clock.tick(60)

        # Jeroen
        DatabaseReceiver.con.commit()
        DatabaseReceiver.con.close()

        # Quit the game when the endless loop ends.
        pygame.quit()
        quit()

# This makes the Boot method like a Main method.
# So that the Boot method is the starting point of the game.
if __name__ == '__main__':
    # Call the constructor of this class.
    Boot().__init__()
