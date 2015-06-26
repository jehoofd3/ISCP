import pygame
from Helpers.Artist import *
from LevelStateManager.LevelStateManager import *

class Boot(object):
    mouse_button_pressed = False

    def __init__(self):
        Artist.begin_session()
        game_exit = False

        clock = pygame.time.Clock()

        lsm = LevelStateManager()

        lsm.run()

        while not game_exit:
            # Event handling
            # Pygame removes events from the queue. pygame.quit argument ensures that only the pygame.quit events are removed.
            for event in pygame.event.get(pygame.QUIT):
                game_exit = True
            Artist.clear_screen()

            lsm.update()
            lsm.draw()

            # Alle objecten renderen
            pygame.display.update()

            # FPS instellen
            clock.tick(60)

        pygame.quit()
        quit()

if __name__ == '__main__':
    Boot().__init__()


