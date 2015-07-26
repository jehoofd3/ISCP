import pygame
from Helpers.Artist import *
from Helpers.DatabaseReceiver import *

class ImageLoader(object):

    def __init__(self, file_name):
        pass

    def get_image(self, x, y, imageNumber):
        image = DatabaseReceiver.get_map_img(str(imageNumber))

        # Weg?
        # Artist.get_display().blit(image, (x, y))


        return image