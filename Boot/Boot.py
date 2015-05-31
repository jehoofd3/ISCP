from GameStateManager.GameStateManager import *
from Helpers.Artist import *


def Boot():

    Artist.begin_session()
    gameExit = False

    clock = pygame.time.Clock()

    gsm = GameStateManager()

    while not gameExit:
        # Event handling
        for event in pygame.event.get():
            # Loop stoppen wanneer het kruisje ingedrukt wordt
            if event.type == pygame.QUIT:
                gameExit = True

        Artist.clear_screen()

        gsm.update()
        gsm.draw()

        # Alle objecten renderen
        pygame.display.update()

        # FPS instellen
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == '__main__':
    Boot()