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

# Author: Richard Jongenburger


class Level1State(LevelState.LevelState):
    map = None
    player = None
    level_state_manager = None
    collider = None
    level_background_music = None
    main_menu = None
    camera = None
    timer = None

    # List to hold all the enemy objects.
    enemy_list = []

    # Spawn point of the player.
    player_spawn_x = 270
    player_spawn_y = 100

    # The X value on which the player needs
    # to be when starting to shift the map and stop shifting the map.
    shift_start = 410
    shift_end = 3290

    cloud_images = []

    # Half the width of the surface.
    # This is needed for the placement of the images/sprites.
    half_screen_width = Artist.get_half_screen_width()

    def __init__(self, level_state_manager, main_menu):
        self.cloud_images = []
        self.enemy_list = []

        # jeroen
        self.map = TileGrid(DatabaseReceiver.get_level_data
                            ("TXT", "Level1", "Level1"))
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

        # jeroen
        self.background = Background(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "BackgroundEen"), 0, 0)

        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud1"), 200, 300, 0.5))
        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud1"), 500, 200, 0.5))
        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud2"), 800, 250, 0.7))
        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud3"), 950, 100, 0.5))
        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud1"), 1200, 300, 0.5))
        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud2"), 1500, 250, 0.5))
        self.cloud_images.append(img.Image(
            DatabaseReceiver.get_level_data(
                "IMAGE", "Level1", "cloud3"), 2000, 500, 0.5))

    def run(self):
        self.map.run()

        # Make the enemy objects and add every enemy to the enemy_list.
        # Every enemy takes a x and y coordinate as argument.(Spawn point)
        # And the range it can walk on the x as.
        # The fish takes a third argument.
        # You got two choices: 'Water' or 'Lava'.
        # According to the fish you want.
        self.enemy_list.append(Fly(500, 600, 100))
        self.enemy_list.append(Fly(1500, 100, 100))
        self.enemy_list.append(Tank(2600, 50, 380))
        self.enemy_list.append(Fish(1000, 700, 200, 'Water'))

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
            pygame.mixer.music.load('../Data/Music/Level4_2.mp3')

        # Play the background music.
        # This is only necessary in level1,
        # because we don't stop the music when creating level2.
        pygame.mixer.music.play()

        # Create a camera for this level.
        self.camera = Camera(self.shift_start, self.shift_end,
                             self.map, self.player, self.enemy_list)

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

        # Draw all the clouds on the surface.
        for cloud in self.cloud_images:
            cloud.draw()

        self.map.draw()

        # Draw all the enemies.
        for e in self.enemy_list:
            e.draw()

        self.player.draw()
        self.timer.draw()

    # Reset the best time with the given level.
    # The best time is in the lower right corner of all the levels.
    def reset_best_time(self):
        self.timer.reset_best_time(1)
