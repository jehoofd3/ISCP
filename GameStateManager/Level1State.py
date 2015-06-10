from Map.TileGrid import *
from Enemy.Fly import *
from Player.Player import *
from Collider.Collider import *


class Level1State(object):
    map = TileGrid("../Data/Levels/ProjectEen.txt", "../Data/Images/Map/SingleSprite.png")
    player = Player(0, 0)
    fly_1 = Fly(100, 0)

    enemy_list = [fly_1]
    collider = Collider(player, map.get_group(), enemy_list)

    def __init__(self):
        pass

    def run(self):
        self.map.run()

    def update(self):
        self.player.update()
        self.fly_1.update()
        self.collider.update()

    def draw(self):
        self.map.draw()
        self.player.draw()
        self.fly_1.draw()
