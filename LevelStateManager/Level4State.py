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


class Level4State(LevelState.LevelState):
    map = None

    player_x = 0
    player_y = 0
    player_spawn_x = 270
    player_spawn_y = 100
    player = Player(player_spawn_x, player_spawn_y)
    enemy_list = []
    level_state_manager = None
    collider = None

    shift_start = 410
    shift_end = 3285

    slime_1 = Slime(64, 150, 0)
    slime_2 = Slime(64, 400, 0)
    slime_3 = Slime(832, 150, 0)
    slime_4 = Slime(832, 400, 0)
    tank_1 = Tank(64, 620, 30)
    tank_2 = Tank(128, 620, 30)
    tank_3 = Tank(250, 620, 30)
    tank_4 = Tank(360, 620, 30)
    tank_5 = Tank(450, 620, 30)
    enemy_list.append(tank_1)
    '''
    enemy_list.append(slime_1)
    enemy_list.append(slime_2)
    enemy_list.append(slime_3)
    enemy_list.append(slime_4)
    enemy_list.append(tank_1)
    enemy_list.append(tank_2)
    enemy_list.append(tank_3)
    enemy_list.append(tank_4)
    enemy_list.append(tank_5)
    '''
    main_menu = None

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.map = TileGrid("../Data/Levels/Level4.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
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

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.states = self.main_menu

    def draw(self):
        self.background.draw()
        self.map.draw()
        for e in self.enemy_list:
            e.draw()

        self.player.draw()
