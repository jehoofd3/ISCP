from PlayerState import *
from PlayerNormalState import *
from Helpers.Artist import *


class PlayerDieState(PlayerState):

    def __init__(self, player):
        super(PlayerDieState, self).__init__(player)
        self.player = player

    def run(self):
        self.player.dead = True
        self.player.jump()

    def update(self):
        self.player.basic_movement()
        self.player.gravity()

        self.player.collision_under = False

        if self.player.rect.bottom >= 960:
            if self.player.lives[0] == self.player.health_image_empty:
                self.player.level_state_manager.player_health = 3
                self.player.level_state_manager.level = 1
                self.player.level_state_manager.open_level1()
            else:
                self.player.level_state_manager.reset_level()

    def draw(self):
        pass
