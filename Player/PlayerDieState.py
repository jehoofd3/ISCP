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

        if self.player.rect.top >= 960:
            self.player.states.pop()
            self.player.states = [PlayerNormalState(self.player)]

    def draw(self):
        pass
