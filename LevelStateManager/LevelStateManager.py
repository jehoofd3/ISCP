from MainMenu.MainMenu import *
from Level2State import *
from Level3State import *
from EndDemo import *
import sys

class LevelStateManager:

    states = ''
    level = 1

    def __init__(self):
        self.states = MainMenu(self)

    def run(self):
        self.states.run()

    def update(self):
        self.states.update()

    def draw(self):
        self.states.draw()

    def next_level(self, main_menu):
        self.level += 1

        if self.level == 4:
            self.states = EndDemo()
        else:
            self.states = getattr(sys.modules[__name__], 'Level' + str(self.level) + 'State')(self, main_menu)

