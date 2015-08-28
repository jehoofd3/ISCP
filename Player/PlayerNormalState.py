import pygame
from PlayerState import *
from Map.TileGrid import *
from Helpers.Artist import *


class PlayerNormalState(PlayerState):
    # Variable that represents the sliding speed.
    # The speed on ice is 8 and the speed on snow is 2.
    player_slide_speed = 0

    def __init__(self, player):
        # This game is object oriented and the class extends from
        # PlayerState so its required to call the super class by using
        # the super() method.
        super(PlayerNormalState, self).__init__(player)

    def run(self):
        # This line of code changes the variable dead in player
        # to False.
        # So the player is alive.
        self.player.dead = False

        # Set the player's x and y on the spawn point of the level.
        self.player.rect.x = self.player.start_x
        self.player.rect.y = self.player.start_y

        # Set the y_speed to 0.
        # The player doesn't weird things when the game starts or when
        # he died.
        self.player.y_speed = 0

    def update(self):
        # The state called the basic_movement and gravity method,
        # so he can move on both axis.
        self.player.basic_movement()
        self.player.gravity()

        # Check if the player is pressing the left arrow key.
        # And to test if you can go to the left.
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and \
                self.player.can_go_left:
            # Set the player's x_speed with the player.speed variable.
            # So the player can move on that speed.
            # We do it minus the player.speed because we go to the left.
            self.player.x_speed -= self.player.speed

            # To set the face_direction variable to Left when the
            # player is going left.
            self.player.face_direction = 'Left'

        # Check if the player is pressing the right arrow key.
        # And to test if you can go to the right.
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and \
                self.player.can_go_right:
            # Set the player's x_speed with the player.speed variable.
            # So the player can move on that speed.
            # We do it plus the player.speed because we go to the right.
            self.player.x_speed += self.player.speed

            # To set the face_direction variable to right when the
            # player is going right.
            self.player.face_direction = 'Right'

        # To make the player slide when it's on snow or ice.
        # First we test if the player is actually on snow or ice.
        # Then we test if the player can go to the left or to the right.
        if (self.player.player_on_snow or self.player.player_on_ice) and \
                self.player.can_go_left and self.player.can_go_right:
            # Set the player's x_speed to the slide_speed.
            self.player.x_speed = self.player_slide_speed

        # If the player has collision with a tile above him.
        if self.player.collision_up:
            # Lower the y_speed with 3 so he doesn't stick to the tile.
            self.player.y_speed = -3

        # If the player is touching a Tile under him,
        # this code will be execute.
        if self.player.collision_under:
            # Because there is a Tile under the player, his y_speed
            # will be set to zero.
            # The gravity will not work, so he stops falling down.
            self.player.y_speed = 0

            # Sometimes the player will float over the map when he
            # touched a Tile this is because of some rounding
            # differences.
            # The bottom (integer) of the player will be divided by the
            # height of a Tile (64).
            # Because rect.bottom is an integer, python will
            # automatically round the outcome.
            # When you multiple the outcome by 64 (Tile height)
            # the rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.player.rect.bottom = ((self.player.rect.bottom / 64) * 64)

            # Change the value of jumps_remaining so the player
            # can jump again
            self.player.jumps_remaining = 1

        # To test if the player pressed on the up arrow key on
        # the keyboard.
        # And if the player still have jumps remaining.
        # If those conditions are met, the player can jump.
        if pygame.key.get_pressed()[pygame.K_UP] and \
                self.player.jumps_remaining > 0:
            # Call the player's jump method in the player class.
            self.player.jump()

            # When you jump, you can to the left and right again,
            # so we set it to True.
            self.player.can_go_left = True
            self.player.can_go_right = True
