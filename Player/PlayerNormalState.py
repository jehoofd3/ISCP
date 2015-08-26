import pygame
from PlayerState import *
from Map.TileGrid import *
from Helpers.Artist import *


class PlayerNormalState(PlayerState):
    # Richard Jongenburger
    player_slide_speed = 0

    def __init__(self, player):
        # This game is object oriented and the class extends from PlayerState,
        # so its required to call the super class by using the super() method.
        super(PlayerNormalState, self).__init__(player)

    def run(self):
        # This line of code changes the variable dead in player to False.
        # So the player is alive.
        self.player.dead = False

        # Richard Jongenburger
        self.player.rect.x = self.player.start_x
        self.player.rect.y = self.player.start_y

        # Set the y_speed to 0.
        # The player doesn't weird things when the game starts or when he died
        self.player.y_speed = 0

    def update(self):
        # The state called the basic_movement and gravity method,
        # so he can move on both axis.
        self.player.basic_movement()
        self.player.gravity()

        # Richard Jongenburger
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and not \
                self.player.canGoLeft:
            self.player.x_speed -= self.player.speed
            self.player.face_direction = 'Left'

        # Richard Jongenburger
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and not \
                self.player.canGoRight:
            self.player.x_speed += self.player.speed
            self.player.face_direction = 'Right'

        if (self.player.player_on_snow or self.player.player_on_ice) \
                and not self.player.canGoLeft and not self.player.canGoRight:
            self.player.x_speed = self.player_slide_speed

        # If the player has collision with a tile above him.
        if self.player.collision_up:
            # Lower the y_speed with 3 so he doesn't stick to the tile.
            self.player.y_speed = -3

        # If the player is touching a Tile under him,
        # this code will be execute.
        if self.player.collision_under:
            # Because there is a Tile under the player, his y_speed will be
            # set to zero.
            # The gravity will not work, so he stops falling down.
            self.player.y_speed = 0

            # Sometimes the player will float over the map when he touched,
            # a Tile this is because of some rounding differences.
            # The bottom (integer) of the player will be divided by the height,
            # of a Tile (64).
            # Because rect.bottom is an integer, python will automatically,
            # round the outcome.
            # When you multiple the outcome by 64 (Tile height),
            # the rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.player.rect.bottom = ((self.player.rect.bottom / 64) * 64)

            # Change the value of jumps_remaining so the player can jump again
            self.player.jumps_remaining = 1

        # Richard Jongenburger
        if pygame.key.get_pressed()[pygame.K_UP] and \
                self.player.jumps_remaining > 0:
            self.player.jump()
            self.player.canGoLeft = True
            self.player.canGoRight = True
