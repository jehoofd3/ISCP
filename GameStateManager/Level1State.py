from Player.Player import *
from Map.TileGrid import *
from GameState import *
__metaclass__ = type


class Level1State(GameState):

    map = TileGrid("ProjectEen.txt")

    def __init__(self, gsm):
        super(Level1State, self).__init__(gsm)

    def run(self):
        print "Lvl1Run"

    def update(self):
        pass

    def draw(self):
        self.map.draw()