from PlayerState import *
from PlayerNormalState import *
from Helpers.Artist import *


class PlayerDieState(PlayerState):

    def __init__(self, player):
        # This game is object oriented and the class extends from EnemyState,
        # so its required
        # to call the super class by using the super() method.
        super(PlayerDieState, self).__init__(player)

    def run(self):
        # This line of code changes the variable dead in player to True.
        # If this variable is True, then the collider stops calculating
        # the collision.
        self.player.dead = True

        # This line of code changes the jumps_remaining to 1.
        # It is needed so the player can jump when he dies.
        self.player.jumps_remaining = 1

        # Call the jump method so the player jumps when he dies.
        self.player.jump()

    def update(self):
        # The state called the basic_movement and gravity method,
        # so he can move on both axis.
        self.player.basic_movement()
        self.player.gravity()

        # If the player's bottom (y coordinate) is bigger then 960.
        # So it's down on the screen.
        # Let the player die. And open or reset a level.
        if self.player.rect.bottom >= 960:
            # If the player don't have lives anymore.
            # Open level 1.
            if self.player.lives[1] == self.player.health_image_empty:
                # Set the player's health back to 3.
                self.player.level_state_manager.player_health = 3

                # Set the level to 1.
                self.player.level_state_manager.level = 1

                # Open level 1.
                self.player.level_state_manager.open_level1()

            # If the do have lives left,
            # after the player died.
            # reset the level.
            else:
                self.player.level_state_manager.reset_level()
