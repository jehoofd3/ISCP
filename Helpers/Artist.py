import pygame

class Artist:

    global game_display
    game_display = pygame.display.set_mode((4000, 768))

    def __init__(self):
        pass

    @staticmethod
    def begin_session():
        pygame.init()
        pygame.display.set_caption("2d Game")

    @staticmethod
    def draw_textures(image, x, y):
        game_display.blit(image, [x, y])

    @staticmethod
    def clear_screen():
        game_display.fill((0, 0, 0))

    @staticmethod
    def get_display():
        return game_display