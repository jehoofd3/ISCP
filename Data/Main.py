from GameStateManager.GameStateManager import *


def Boot():
    beginSession()
    gameExit = False

    clock = pygame.time.Clock()

    gsm = GameStateManager()

    while not gameExit:
        # Event handling
        for event in pygame.event.get():
            # Loop stoppen wanneer het kruisje ingedrukt wordt
            if event.type == pygame.QUIT:
                gameExit = True

         # Scherm wit maken
        #gameDisplay.fill(255, 255, 255)

        print clock.get_fps()

        gsm.update()
        gsm.draw()

        # Alle objecten renderen
        pygame.display.update()

        # FPS instellen
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == '__main__': Boot()