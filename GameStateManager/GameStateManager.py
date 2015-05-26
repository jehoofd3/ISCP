from Level1State import *


class GameStateManager:

    states = []

    def __init__(self):
        self.states = [Level1State()]
        self.run()

    def update(self):
        self.states[0].update()

    def draw(self):
        self.states[0].draw()

    def run(self):
        self.states[0].run()

    def setCurrentState(self, newCurrentState):
        self.states[0] = globals()[newCurrentState]()
        self.run()