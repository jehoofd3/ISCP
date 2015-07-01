import pygame

class Artist:

    # Window dimensions
    screen_width = 960
    screen_height = 768
    bi = 0

    # Make a window with the specified with and height.
    global game_display
    game_display = pygame.display.set_mode((screen_width, screen_height))

    def __init__(self):
        pass

    @staticmethod
    def begin_session():
        # Initialize all imported pygame modules
        pygame.init()

        pygame.display.set_caption("Escape")

    @staticmethod
    def draw_textures(image, x, y):
        game_display.blit(image, [x, y])

    @staticmethod
    def clear_screen():
        game_display.fill((0, 0, 0))

    @staticmethod
    def get_display():
        return game_display

    @staticmethod
    def get_screen_width():
        return Artist.screen_width

    @staticmethod
    def get_screen_height():
        return Artist.screen_height

    @staticmethod
    def get_half_screen_width():
        return Artist.screen_width / 2

    @staticmethod
    def get_half_screen_height():
        return Artist.screen_height / 2

    @staticmethod
    def get_bi():
        Artist.bi += 1
        return Artist.bi



