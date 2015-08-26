from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from MainMenu.MainMenu import *
from Parallax.Background import *
from Helpers.DatabaseReceiver import *

# Author: Richard Jongenburger


class Level3State(LevelState.LevelState):
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
    player_spawn_x = 170
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
        self.enemy_list = []
        # jeroen
        self.map = TileGrid(DatabaseReceiver.get_level_data
                            ("TXT", "Level3", "Level3"))
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
                "IMAGE", "Level3", "BackgroundDrie"), 0, 0)

    def run(self):
        self.map.run()
        self.enemy_list = []

        # Make the enemy objects and add every enemy to the enemy_list.
        # Every enemy takes a x and y coordinate as argument.(Spawn point)
        # And the range it can walk on the x as.
        # The fish takes a third argument.
        # You got two choices: 'Water' or 'Lava'.
        # According to the fish you want.
        self.enemy_list.append(Slime(1100, 10))
        self.enemy_list.append(Tank(2200, 400, 450))
        self.enemy_list.append(Fly(3000, 50, 300))

        # Add a collider for the enemies and the player.
        # It takes the player, map group(tiles),
        # an array with all the enemy objects, Reference to LevelStateManager
        # as arguments.
        self.collider = Collider(self.player, self.map.get_group(),
                                 self.enemy_list, self.LevelStateManager)

        # Create a camera for this level.
        self.camera = Camera(self.shift_start, self.shift_end,
                             self.map, self.player, self.enemy_list)

        # Create a timer for this level.
        self.timer = Timer()

        # Load the best time of level 1.
        self.timer.load_best_time(3)

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

        # Create a camera for this level.
        self.camera = Camera(self.shift_start, self.shift_end,
                             self.map, self.player, self.enemy_list)

        # Create a timer for this level.
        self.timer = Timer()

        # Load the best time of level 1.
        self.timer.load_best_time(1)

    def draw(self):
        self.background.draw()
        self.map.draw()

        # Draw all the enemies.
        for e in self.enemy_list:
            e.draw()

        self.player.draw()
        self.timer.draw()

    # Reset the best time with the given level.
    # The best time is in the lower right corner of all the levels.
    def reset_best_time(self):
        self.timer.reset_best_time(3)
