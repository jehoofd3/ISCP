import pygame
from Helpers.Artist import *


class Parallax(object):

    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert()
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x -= x/4
        self.y -= y/4

    def draw(self):
        Artist.get_display().blit(self.image, [self.x, self.y])
