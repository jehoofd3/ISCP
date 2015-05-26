import os
import pygame

gameDisplay = pygame.display.set_mode((960, 768))


def beginSession():
    pygame.init()
    pygame.display.set_caption("2d Game")

    # Zonder parameters wordt het hele scherm elke frame opnieuw getekend
    pygame.display.update()


def drawTextures(path, x, y, width, height):
    image = pygame.image.load(os.path.join(path))
    image.convert()

    gameDisplay.blit(image, [x, y])

def clearScreen():
    pass