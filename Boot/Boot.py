from GameStateManager.LevelStateManager import *
from Player.PlayerStateManager import *

class Boot(object):

    def __init__(self):
        Artist.begin_session()
        game_exit = False

        clock = pygame.time.Clock()

        gsm = LevelStateManager()
        psm = PlayerStateManager()

        while not game_exit:
            # Event handling
            for event in pygame.event.get():
                # Loop stoppen wanneer het kruisje ingedrukt wordt
                if event.type == pygame.QUIT:
                    game_exit = True

            Artist.clear_screen()

            #GameStateManager
            gsm.update()
            gsm.draw()

            #PlayerStateManager
            psm.update()
            psm.draw()

            # Alle objecten renderen
            pygame.display.update()

            # FPS instellen
            clock.tick(60)

        pygame.quit()
        quit()

if __name__ == '__main__':
    Boot().__init__()
