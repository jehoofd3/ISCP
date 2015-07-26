import pygame
from Helpers.Artist import *


class Parallax(object):

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def update(self, x, y, player_x):
        if player_x >= Artist.get_half_screen_width() - 80:
            self.x -= x/4
            self.y -= y/4

    def draw(self):
        Artist.draw_textures(self.image, [self.x, self.y])
