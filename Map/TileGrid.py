from Map.Tile import *
from Helpers.Artist import *

class TileGrid():
    map = [[x for x in range(12)] for y in range(60)]
    rows = len(map)
    collums = len(map[0])

    def __init__(self, levelPath):

        file = open(levelPath)
        for i in range (self.collums):
            for j in range (self.rows):
                self.map[j][i] = Tile(j * 64, i * 64, file.next()[:-1])
        print self.map

    def draw(self):
        for i in range (self.collums):
            for j in range (self.rows):
                self.map[j][i].draw()