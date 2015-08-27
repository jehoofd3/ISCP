from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from MainMenu.MainMenu import *
from Parallax.Background import *
from Helpers.DatabaseReceiver import *

# Author: Richard Jongenburger


class Level4State(LevelState.LevelState):
    map = None
    player = None
    level_state_manager = None
    collider = None
    level_background_music = None
    main_menu = None
    timer = None

    # List to hold all the enemy objects.
    enemy_list = []

    # Spawn point of the player.
    player_spawn_x = 256
    player_spawn_y = 0

    # Half the width of the surface.
    # This is needed for the placement of the images/sprites.
    half_screen_width = Artist.get_half_screen_width()

    next_lvl_list = []

    def __init__(self, level_state_manager, main_menu):
        self.next_lvl_list = []
        self.enemy_list = []
        # jeroen
        self.map = TileGrid(DatabaseReceiver.get_level_data
                            ("TXT", "Level4", "Level4"))
        self.main_menu = main_menu
        self.LevelStateManager = level_state_manager

        # Create a player object with the x and y
        # value in which the player should spawn and the LevelStateManager.
        self.player = Player(self.player_spawn_x,
                             self.player_spawn_y,
                             level_state_manager)

        # Statement to set the player_x variable in the map class.
        # It is necessary for the camera
        # that the map knows the x coordinate of the spawn point.
        self.map.set_player_x(self.player_spawn_x)

        # Jeroen
        self.background = Background(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level4", "background1"))

        # Jeroen
        self.background_text = DatabaseReceiver.get_level_data(
            "IMAGE", "Level4", "YouCantWin")

    def run(self):
        self.enemy_list = []

        # Make the enemy objects and add every enemy to the enemy_list.
        # Every enemy takes a x and y coordinate as argument.(Spawn point)
        # And the range it can walk on the x as.
        # The fish takes a third argument.
        # You got two choices: 'Water' or 'Lava'.
        # According to the fish you want.
        self.enemy_list.append(Slime(64, 100))
        self.enemy_list.append(Slime(95, 400))
        self.enemy_list.append(Slime(832, 150))
        self.enemy_list.append(Slime(820, 400))
        self.enemy_list.append(Tank(100, 600, 700))
        self.enemy_list.append(Tank(200, 600, 500))
        self.enemy_list.append(Tank(300, 600, 200))
        self.enemy_list.append(Tank(80, 600, 700))
        self.enemy_list.append(Tank(100, 600, 700))

        # Add a collider for the enemies and the player.
        # It takes the player, map group(tiles),
        # an array with all the enemy objects, Reference to LevelStateManager
        # as arguments.
        self.collider = Collider(self.player, self.map.get_group(),
                                 self.enemy_list, self.LevelStateManager)

        # Load the background music.
        # The pygame.mixer.music.load
        # method takes the file location as an argument.
        # It has to be .wav or .mp3.
        self.level_background_music = \
            pygame.mixer.music.load('../Data/Music/Level4_3.mp3')

        # Play the background music.
        pygame.mixer.music.play()

        # Create a timer for this level.
        self.timer = Timer()

        # Load the best time of level 1.
        self.timer.load_best_time(1)

    def update(self):
        # Update the camera with the player's x speed.
        self.camera.update_camera(self.player.x_speed)
        self.timer.update()

        self.player.update()

        # Update all the enemies in the enemy_list.
        self.enemy_list = self.collider.enemy_list
        for e in self.enemy_list:
            e.update()

        self.collider.update()

        self.background.update(self.player.x_speed, 0, self.player.rect.x)

        # Update the clouds.
        for image in self.cloud_images:
            image.update(self.player.x_speed, 0, self.player.rect.x)

        # Opens the MainMenu when you press on the escape key.
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.LevelStateManager.level_state = self
            self.LevelStateManager.states = self.main_menu

    def draw(self):
        self.background.draw()
        self.map.draw()

        Artist.draw_textures(self.background_text, (300, 200))

        # Draw all the enemies.
        for e in self.enemy_list:
            e.draw()

        self.player.draw()
        self.timer.draw()

    # Reset the best time with the given level.
    # The best time is in the lower right corner of all the levels.
    def reset_best_time(self):
        self.timer.reset_best_time(4)
