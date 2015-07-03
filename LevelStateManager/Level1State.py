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
from Parallax.Background import *
from MainMenu.MainMenu import *

class Level1State(LevelState.LevelState):
    map = None

    player_x = 0
    player_y = 0
    player_spawn_x = 270
    player_spawn_y = 100
    player = None
    enemy_list = []
    level_state_manager = None
    collider = None

    shift_start = 410
    shift_end = 3285

    fly = Fly(100, 300, 0)
    slime_2 = Slime(64, 400, 0)
    slime_3 = Slime(832, 150, 0)
    slime_4 = Slime(832, 400, 0)
    tank_1 = Tank(164, 200, 30)
    tank_2 = Tank(128, 620, 30)
    tank_3 = Tank(250, 620, 30)
    tank_4 = Tank(360, 620, 30)
    tank_5 = Tank(450, 620, 30)
    enemy_list.append(fly)

    main_menu = None

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.map = TileGrid("../Data/Levels/Level1.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)
        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)
        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background("../Data/Levels/BackgroundEen.png", 0, 0)

    def run(self):
        self.map.run()

    def update(self):
        self.player.update()

        for e in self.enemy_list:
            e.update()

        self.collider.update()

        self.background.update(self.player.xSpeed, 0)
        # Code that it will only shift between the given values
        if not self.player.is_shifting:
            self.map.x_start_shift_map += self.player.xSpeed

        if self.shift_start <= self.map.x_start_shift_map <= self.shift_end:
            self.player.is_shifting = True
            self.map.shift_map(self.player.get_player_x_speed())

            for e in self.enemy_list:
                e.move_with_map(self.player.get_player_x_speed())

        else:
            self.player.is_shifting = False
        # end shift map

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.states = self.main_menu

    def draw(self):
        self.background.draw()
        self.map.draw()

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
