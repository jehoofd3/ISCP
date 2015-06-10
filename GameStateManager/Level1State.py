from Map.TileGrid import *
from Enemy.Fly import *


class Level1State(object):

    map = TileGrid("../Data/Levels/ProjectEen.txt", "../Data/Images/Map/SingleSprite.png")
    fly_1 = Fly(0, 0)

    def __init__(self):
        pass

    def run(self):
        self.map.run()

    def update(self):
        self.fly_1.update()
        '''
        code om nieuwe level te openen
        '''

    def draw(self):
        self.map.draw()
        self.fly_1.draw()
