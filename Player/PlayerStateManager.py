from PlayerNormalState import *

class PlayerStateManager(object):

    states = []

    def __init__(self):
        self.states = [PlayerNormalState()]
        self.run()

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        self.states[0].draw()
