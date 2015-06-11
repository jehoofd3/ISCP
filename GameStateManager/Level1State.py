from Map.TileGrid import *
from Enemy.Fly import *
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *

class Level1State(object):
    map = TileGrid("../Data/Levels/ProjectEen.txt", "../Data/Images/Map/SingleSprite.png")
    player = Player(240, 546)
    fly_1 = Fly(100, 0)

    enemy_list = [fly_1]
    collider = Collider(player, map.get_group(), enemy_list)

    player_x = 0
    player_y = 0

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self):
        pass

    def run(self):
        self.map.run()

    def update(self):
        self.player.update()
        self.fly_1.update()
        self.collider.update()

        if self.player.get_player_x() >= self.half_screen_width:
            self.map.shift_map(self.player.get_player_x_speed())

    def draw(self):
        self.map.draw()
        self.player.draw()
        self.fly_1.draw()
