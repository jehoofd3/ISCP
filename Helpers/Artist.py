import pygame

class Artist:

    screen_width = 960
    screen_height = 768

    global game_display
    game_display = pygame.display.set_mode((screen_width, screen_height))

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

    #70 is player width
    @staticmethod
    def get_half_screen_width():
        return (Artist.screen_width / 2) - 70
