from Player.Player import *
from Map.TileGrid import *


class Level1State():
    map = TileGrid("Data/Levels/LevelEen.txt");
    player = Player(100, 100, 0, 0, "Test.png")

    def __init__(self):
        pass

    def run(self):
        print "Lvl1 run()"

    def update(self):
        self.player.update()

    def draw(self):

        self.map.draw()
        self.player.draw()