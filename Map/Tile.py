from Helpers.Artist import *


class Tile():
    x = 0
    y = 0
    image = " "

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        Artist.draw_textures(self.image, self.x, self.y)
