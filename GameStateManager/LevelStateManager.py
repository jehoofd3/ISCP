from Level1State import *
from Level2State import *


class LevelStateManager:

    states = []

    def __init__(self):
        self.states = [Level1State()]
        self.run()

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        self.states[0].draw()

    @staticmethod
    def switch_state():
        LevelStateManager.states[0] = Level2State()
