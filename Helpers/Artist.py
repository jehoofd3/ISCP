import pygame

# Author: Richard Jongenburger


class Artist(object):

    # Window dimensions
    screen_width = 960
    screen_height = 768

    # jeroen
    bi = 0

    global game_display

    # Makes a window with the specified width and height.
    game_display = pygame.display.set_mode((screen_width, screen_height))

    def __init__(self):
        pass

    @staticmethod
    def begin_session():

        # Initialize all imported pygame modules.
        pygame.init()

        # Sets a title to the window.
        pygame.display.set_caption("Escape")

    @staticmethod
    def draw_textures(image, rect):
        # This pygame method draws an image on the surface.
        # It takes an image as the first argument.
        # And a rectangle object in the second argument.
        game_display.blit(image, rect)

    # jeroen
    @staticmethod
    def rotate_img(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        # In left veranderen?!
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
