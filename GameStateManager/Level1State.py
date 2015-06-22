from Map.TileGrid import *
import LevelState
from Enemy.Fly import *
from Enemy.Fish import *
from Enemy.Slime import *
from Enemy.Snake import *
from Enemy.Tank import *
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *

class Level1State(LevelState.LevelState):
    map = TileGrid("../Data/Levels/ProjectEen.txt", "../Data/Images/Map/SingleSprite.png")
    player = Player(140, 400)
    slime_1 = Slime(500, 500, 10)

    enemy_list = []
    collider = Collider(player, map.get_group(), enemy_list)

    player_x = 0
    player_y = 0

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level):
        super(Level1State, self).__init__(level)

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
