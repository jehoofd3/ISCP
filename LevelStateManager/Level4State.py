from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from MainMenu.MainMenu import *
from Parallax.Background import *

class Level4State(LevelState.LevelState, Camera):
    map = None

    player_x = 0
    player_y = 0
    player_spawn_x = 256
    player_spawn_y = 0
    player = None
    enemy_list = []
    level_state_manager = None
    collider = None

    shift_start = 410
    shift_end = 3290

    main_menu = None

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.enemy_list = []
        self.map = TileGrid("../Data/Levels/Level4/Level4.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)
        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background("../Data/Levels/Level1/BackgroundEen.png", 0, 0)

    def run(self):
        tank_x = 100
        tank_y = 620
        tank_range = 700
        self.map.run()
        self.enemy_list = []
        fly = Fly(150, 150, 0)
        slime_1 = Slime(64, 100)
        slime_2 = Slime(64, 400)
        slime_3 = Slime(832, 150)
        slime_4 = Slime(832, 400)
        tank_2 = Tank(tank_x, tank_y, tank_range)
        tank_3 = Tank(tank_x, tank_y, tank_range)
        tank_4 = Tank(tank_x, tank_y, tank_range)
        tank_5 = Tank(tank_x, tank_y, tank_range)
#        self.enemy_list.append(fly)
        self.enemy_list.append(slime_1)
        self.enemy_list.append(slime_2)
        self.enemy_list.append(slime_3)
        self.enemy_list.append(slime_4)
#        self.enemy_list.append(tank_2)
#        self.enemy_list.append(tank_3)
#        self.enemy_list.append(tank_4)
#        self.enemy_list.append(tank_5)

        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)

    def update(self):
        self.player.update()
        self.enemy_list = self.collider.enemy_list

        for e in self.enemy_list:
            e.update()

        self.collider.update()

        self.background.update(0, 0, self.player.xSpeed)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.states = self.main_menu

    def draw(self):
        self.background.draw()
        self.map.draw()

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
