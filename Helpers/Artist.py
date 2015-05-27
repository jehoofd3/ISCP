import os
import pygame


class Artist:

    global gameDisplay
    gameDisplay = pygame.display.set_mode((960, 768))

    @staticmethod
    def begin_session():
        pygame.init()
        pygame.display.set_caption("2d Game")

    @staticmethod
    def draw_textures(image, x, y):
        gameDisplay.blit(image, (x, y))

    def clear_screen(self):
        gameDisplay.fill((255, 255, 255))


