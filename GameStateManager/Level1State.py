from Map.TileGrid import *


class Level1State(object):

    map = TileGrid("../Data/Levels/ProjectEen.txt", "../Data/Images/Map/SingleSprite.png")

    def __init__(self):
        pass

    def run(self):
        self.map.run()

    def update(self):
        '''
        code om nieuwe level te openen
        '''

    def draw(self):
        self.map.draw()
