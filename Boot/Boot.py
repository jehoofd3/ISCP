import pygame


class Boot:

    clock = pygame.time.Clock()

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    Boot()