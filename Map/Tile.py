from Map.ColliderType import *
from Helpers.Artist import *

class Tile():
    x = 0
    y = 0
    imagePath = " "
#    cType = ColliderType


    def __init__(self, x, y, imagePath):
        self.x = x
        self.y = y
        self.imagePath = imagePath

    def draw(self):
        drawTextures(self.imagePath, self.x, self.y, 64, 64)

    def setcType(self, cType):
        self.cType = cType