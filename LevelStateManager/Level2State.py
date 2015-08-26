from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from Parallax.Background import *
from MainMenu.MainMenu import *
from Camera import *
from Helpers.DatabaseReceiver import *

class Level2State(LevelState.LevelState):
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

    camera = None
    timer = None

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.enemy_list = []
        self.map = TileGrid(DatabaseReceiver.get_level_data("TXT", "Level2", "Level2"))
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager

        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)

        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background(DatabaseReceiver.get_level_data("IMAGE", "Level2", "BackgroundTwee"))

    def run(self):
        self.map.run()
        self.enemy_list = []
        fish = Fish(580, 600, 110, "Lava")
        fish2 = Fish(2570, 600, 400, "Lava")
        slime = Slime(1736, 10)
        self.enemy_list.append(slime)
        self.enemy_list.append(fish)
        self.enemy_list.append(fish2)

        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager)

        self.camera = Camera(self.shift_start, self.shift_end, self.map, self.player, self.enemy_list)

        self.timer = Timer()
        self.timer.load_best_time(2)

    def update(self):
        self.camera.update_camera(self.player.x_speed)
        self.timer.update()

        self.player.update()
        self.enemy_list = self.collider.enemy_list
        for e in self.enemy_list:
            e.update()

        self.collider.update()
        self.background.update(0, 0, self.player.x_speed)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.level_state = self
            self.level_state_manager.states = self.main_menu

    def draw(self):
        self.background.draw()
        self.map.draw()

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
        self.timer.draw()

    def reset_best_time(self):
        self.timer.reset_best_time(2)