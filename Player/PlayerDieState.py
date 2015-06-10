from PlayerState import *


class PlayerDieState(PlayerState):

    def __init__(self, player):
        super(PlayerDieState, self).__init__(player)
        self.player = player

    def run(self):
        print "RUN"

    def update(self):
        print "UPDATE"

    def draw(self):
        pass