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
from MainMenu.MainMenu import *

class Level1State(LevelState.LevelState):
    map = None

    player_x = 0
    player_y = 0
    player_spawn_x = 270
    player_spawn_y = 100
    player = Player(player_spawn_x, player_spawn_y)
    enemy_list = []
    level_state_manager = None
    collider = None
    background_image = pygame.image.load("../Data/Levels/BackgroundEen.png").convert()

    shift_start = 410
    shift_end = 3290

    fly = Fly(180, 50, 10)

    main_menu = None

    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.map = TileGrid("../Data/Levels/Level1.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)
        self.map.set_x_start_shift_map(self.player_spawn_x)

    def run(self):
        self.map.run()

    def update(self):
        self.player.update()
        self.fly.update()

        for e in self.enemy_list:
            e.update()

        self.collider.update()

        # Code that it will only shift between the given values
        if not self.player.is_shifting:
            self.map.x_start_shift_map += self.player.xSpeed

        if self.map.x_start_shift_map >= self.shift_start and self.map.x_start_shift_map <= self.shift_end:
            self.player.is_shifting = True
            self.map.shift_map(self.player.get_player_x_speed())
        else:
            self.player.is_shifting = False
        # end shift map

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.states = self.main_menu

    def draw(self):
        Artist.get_display().blit(self.background_image, [0, 0])
        self.map.draw()
        self.fly.draw()
        for e in self.enemy_list:
            e.draw()

        self.player.draw()