from Map.TileGrid import *
from Enemy.Fly import *
from Enemy.Fish import *
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *

class Level1State(object):
    map = TileGrid("../Data/Levels/ProjectEen.txt", "../Data/Images/Map/SingleSprite.png")
    player = Player(140, 400)
    fly_1 = Fly(300, 600, 200)
    fish_1 = Fish(300, 700, 200)

    enemy_list = [fish_1, fly_1]
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
        for e in self.enemy_list:
            e.update()

        self.collider.update()

        if self.player.get_player_x() >= self.half_screen_width:
            self.map.shift_map(self.player.get_player_x_speed())

    def draw(self):
        self.map.draw()

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
