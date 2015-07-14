import pygame

class Artist(object):

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
        # Initializes all imported pygame modules.

        # No exceptions will be raised if a module fails, but the total number if successful and failed inits will be returned as a tuple.
        # You can always initialize individual modules manually, but pygame.init()initialize all imported pygame modules is a convenient way to get everything started.
        # The init() functions for individual modules will raise exceptions when they fail.
        # You may want to initalise the different modules seperately to speed up your program or to not use things your game does not.
        #It is safe to call this init() more than once: repeated calls will have no effect. This is true even if you have pygame.quit() all the modules.
        pygame.init()

        # Gives a title to the window.
        pygame.display.set_caption("Escape")

    @staticmethod
    def draw_textures(image, rect):
        # This pygame method draws an image on the surface.
        game_display.blit(image, rect)

    @staticmethod
    def rotate_img(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)

        Artist.draw_textures(rot_image, rect)

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
