from Level1State import *


class GameStateManager (object):

    states = []

    def __init__(self, state):
        self.states = state
 
    def update(self):
        self.states[0].update()

    def draw(self):
        self.states[0].draw()

    def run(self):
        self.states[0].run()
