from Helpers.Artist import *


class Tile():
    x = 0
    y = 0

    def __init__(self, x, y, imagePath):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imagePath).convert_alpha()

    def draw(self):
        Artist.draw_textures(self.image, self.x, self.y)
