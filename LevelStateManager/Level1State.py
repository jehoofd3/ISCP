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
from Camera import *
from Timer import *
import Parallax.Image as img
from Helpers.DatabaseReceiver import *

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
    level_background_music = None

    main_menu = None
    image_list = []

    camera = None
    timer = None

    half_screen_width = Artist.get_half_screen_width()

    # Geen super call???
    def __init__(self, level_state_manager, main_menu):
        self.image_list = []
        self.enemy_list = []
        self.map = TileGrid(DatabaseReceiver.get_level_data("TXT", "Level1", "Level1"))
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)
        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background(DatabaseReceiver.get_level_data("IMAGE", "Level1", "BackgroundEen"), 0, 0)

        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud1"), 200, 300, 0.5))
        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud1"), 500, 200, 0.5))
        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud2"), 800, 250, 0.7))
        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud3"), 950, 100, 0.5))
        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud1"), 1200, 300, 0.5))
        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud2"), 1500, 250, 0.5))
        self.image_list.append(img.Image(DatabaseReceiver.get_level_data("IMAGE", "Level1", "cloud3"), 2000, 500, 0.5))

    def run(self):
        self.map.run()
        fly_1 = Fly(500, 600, 100)
        fly_2 = Fly(1500, 100, 100)
        tank = Tank(2600, 50, 380)
        fish = Fish(1000, 700, 200)
        self.enemy_list.append(fly_1)
        self.enemy_list.append(fly_2)
        self.enemy_list.append(tank)
        self.enemy_list.append(fish)
        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)

        self.level_background_music = pygame.mixer.music.load('../Data/Music/Level4_2.mp3')
        pygame.mixer.music.play()

        self.camera = Camera(self.shift_start, self.shift_end, self.map, self.player, self.enemy_list)

        self.timer = Timer()
        self.timer.load_best_time(1)

    def update(self):
        self.camera.update_camera(self.player.xSpeed)
        self.timer.update()

        self.player.update()
        self.enemy_list = self.collider.enemy_list
        for e in self.enemy_list:
            e.update()

        self.collider.update()

        self.background.update(self.player.xSpeed, 0, self.player.rect.x)
        for image in self.image_list:
            image.update(self.player.xSpeed, 0, self.player.rect.x)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.level_state = self
            self.level_state_manager.states = self.main_menu

    def draw(self):
        self.background.draw()
        for image in self.image_list:
            image.draw()

        self.map.draw()

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
        self.timer.draw()

    def reset_best_time(self):
        self.timer.reset_best_time(1)
