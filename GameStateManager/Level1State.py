from Player.Player import *
from Map.TileGrid import *
from GameState import *
from Player import *
import socket
__metaclass__ = type


class Level1State(GameState):

    map = TileGrid("ProjectEen.txt")
    player = Player(10, 10, "Image/Player/Loop/8.png")

    def __init__(self, gsm):
        super(Level1State, self).__init__(gsm)

    def run(self):
        print "Lvl1Run"

    def update(self):
        self.player.update()

    def draw(self):
        self.map.draw()
        self.player.draw()