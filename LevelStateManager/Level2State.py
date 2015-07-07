from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from Parallax.Background import *
from MainMenu.MainMenu import *
from Camera import *

class Level2State(LevelState.LevelState, Camera):
    map = None

    player_x = 0
    player_y = 0
    player_spawn_x = 170
    player_spawn_y = 180
    player = None
    enemy_list = []
    level_state_manager = None
    collider = None

    shift_start = 410
    shift_end = 3290

    main_menu = None

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.map = TileGrid("../Data/Levels/Level2.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager

        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)

        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background("../Data/Levels/BackgroundTwee.png", 0, 0)

    def run(self):
        self.map.run()
        self.enemy_list = []
        slime = Slime(1736, 10)
        slime.delete_snake_list()
        self.enemy_list.append(slime)

        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)
        Camera.__init__(self, self.shift_start, self.shift_end, self.map, self.player, self.enemy_list)

    def update(self):
        Camera.update(self)
        self.player.update()
        self.enemy_list = self.collider.enemy_list
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
