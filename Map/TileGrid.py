from Map.Tile import *
from Helpers.Artist import *

class TileGrid():
    map = [None] * 720

    global image_location

    def __init__(self, levelPath):
        with open("../Levels/" + levelPath, "r") as f:
            self.image_location = f.read().splitlines()

        level_images = []
        for image in self.image_location:
            level_images.append(pygame.image.load("../" + image).convert_alpha())

        x = 0
        y = 0
        for count in range(len(level_images)):
            self.map[count] = Tile(x, y, level_images[count])
            x = x + 64

            if count % 60 == 0 and count != 0:
                y = y + 64
                x = 0

    def draw(self):
         for count in range(0, 720):
            if self.image_location[count] != "Image/Empty.png":
                self.map[count].draw()











