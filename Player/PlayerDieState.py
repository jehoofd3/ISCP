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

        # Kan als het goed is weg.
       # self.player.collision_under = False

        # Richard Jongenburger crap code
        if self.player.rect.bottom >= 960:
            if self.player.lives[1] == self.player.health_image_empty:
                self.player.level_state_manager.player_health = 3
                self.player.level_state_manager.level = 1
                self.player.level_state_manager.open_level1()
            else:
                self.player.level_state_manager.reset_level()
