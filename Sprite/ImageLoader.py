import pygame
from Helpers.Artist import *

class ImageLoader(object):

    def __init__(self, file_name):
        pass

    def get_image(self, x, y, imageNumber):

        image = pygame.image.load("../Data/Images/Map/" + str(imageNumber) + ".png").convert_alpha()

        Artist.get_display().blit(image, (x, y))

        return image