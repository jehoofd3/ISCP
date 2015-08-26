import pygame
from Helpers.Artist import *


class Parallax(object):

    # This constructor takes three variables.
    # The image variable is an image.
    # The x and y variables are integers and
    # is used to set the location of the image.
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    # The update method is used to update the location of the image.
    def update(self, x, y, player_x):

        # If the player's x location is greater than the
        # half screen width minus 80 (the width of the player).
        # Than the parallax effect starts
        if player_x >= Artist.get_half_screen_width() - 80:
            self.x -= x/4
            self.y -= y/4

    # This method draws the image on the screen.
    def draw(self):
        # Use the method draw_textures in Artist.
        # This draws the image to the screen.
        Artist.draw_textures(self.image, [self.x, self.y])
