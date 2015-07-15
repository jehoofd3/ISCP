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
    background_text = None
    main_menu = None
    level_background_music = None
    half_screen_width = Artist.get_half_screen_width()
    next_lvl_list = []

    def __init__(self, level_state_manager, main_menu):
        self.next_lvl_list = []
        self.enemy_list = []
        self.map = TileGrid("../Data/Levels/Level4/Level4.txt")
        self.main_menu = main_menu
        self.level_state_manager = level_state_manager
        self.player = Player(self.player_spawn_x, self.player_spawn_y, level_state_manager)
        self.map.set_x_start_shift_map(self.player_spawn_x)
        self.background = Background("../Data/Levels/Level4/background1.png", 0, 0)
        self.background_text = pygame.image.load("../Data/Levels/Level4/YouCantWin.png").convert_alpha()

    def run(self):
        self.enemy_list = []

        self.enemy_list.append(Slime(64, 100))
        self.enemy_list.append(Slime(95, 400))
        self.enemy_list.append(Slime(832, 150))
        self.enemy_list.append(Slime(820, 400))
        self.enemy_list.append(Tank(100, 600, 700))
        self.enemy_list.append(Tank(200, 600, 500))
        self.enemy_list.append(Tank(300, 600, 200))
        self.enemy_list.append(Tank(80, 600, 700))
        self.enemy_list.append(Tank(100, 600, 700))

        self.collider = Collider(self.player, self.map.get_group(), self.enemy_list, self.level_state_manager, self.main_menu)

        self.level_background_music = pygame.mixer.music.load('../Data/Music/Level4_3.mp3')
        pygame.mixer.music.play()

    def update(self):
        self.player.update()
        self.enemy_list = self.collider.enemy_list

        for e in self.enemy_list:
            e.update()

        self.collider.update()

        self.background.update(0, 0, self.player.xSpeed)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.level_state_manager.states = self.main_menu

        self.next_lvl_list = [None] * len(self.enemy_list)
        for i in range(len(self.enemy_list)):
            self.next_lvl_list[i] = self.enemy_list[i].dead

        if all(self.next_lvl_list):
            self.level_state_manager.next_level()

    def draw(self):
        self.background.draw()
        self.map.draw()

        Artist.draw_textures(self.background_text, (300, 200))

        for e in self.enemy_list:
            e.draw()

        self.player.draw()
