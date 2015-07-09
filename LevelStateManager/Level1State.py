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
from Parallax.Image import *
from MainMenu.MainMenu import *
from Camera import *

class Level1State(LevelState.LevelState, Camera):
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

    main_menu = None
    image_list = []

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.image_list = []
        self.enemy_list = []
        self.map = TileGrid("../Data/Levels/Level1/Level1.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)
        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background("../Data/Levels/Level1/BackgroundEen.png", 0, 0)

        self.image_list.append(Image("../Data/Levels/Level1/cloud1.png", 200, 300, 0.5))
        self.image_list.append(Image("../Data/Levels/Level1/cloud1.png", 500, 200, 0.5))
        self.image_list.append(Image("../Data/Levels/Level1/cloud2.png", 800, 250, 0.7))
        self.image_list.append(Image("../Data/Levels/Level1/cloud3.png", 950, 100, 0.5))
        self.image_list.append(Image("../Data/Levels/Level1/cloud1.png", 1200, 300, 0.5))
        self.image_list.append(Image("../Data/Levels/Level1/cloud2.png", 1500, 250, 0.5))
        self.image_list.append(Image("../Data/Levels/Level1/cloud3.png", 2000, 500, 0.5))

    def run(self):
        self.map.run()
        fly = Fly(1500, 100, 100)
        tank = Tank(2600, 50, 380)
        fish = Fish(1000, 700, 200)
        self.enemy_list.append(fly)
        self.enemy_list.append(tank)
        self.enemy_list.append(fish)
        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)
        Camera.__init__(self, self.shift_start, self.shift_end, self.map, self.player, self.enemy_list)

    def update(self):
        Camera.update_camera(self, self.player.xSpeed)
        self.player.update()
        self.enemy_list = self.collider.enemy_list
        for e in self.enemy_list:
            e.update()

        self.collider.update()

        self.background.update(self.player.xSpeed, 0, self.player.rect.x)
        for image in self.image_list:
            image.update(self.player.xSpeed, 0, self.player.rect.x)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.states = self.main_menu

    def draw(self):
        self.background.draw()
        for image in self.image_list:
            image.draw()

        self.map.draw()

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
