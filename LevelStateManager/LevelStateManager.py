from MainMenu.MainMenu import *
from Level2State import *
from Level3State import *
from EndDemo import *
import sys

class LevelStateManager:

    states = ''
    level = 1
    main_menu = None

    def __init__(self):
        self.states = MainMenu(self)
        self.main_menu = self.states

    def run(self):
        self.states.run()

    def update(self):
        self.states.update()

    def draw(self):
        self.states.draw()

    def next_level(self):
        self.level += 1

        if self.level == 5:
            self.states = EndDemo()
        else:
            self.states = getattr(sys.modules[__name__], 'Level' + str(self.level) + 'State')(self, self.main_menu)

    def reset_level(self):
        self.states = getattr(sys.modules[__name__], 'Level' + str(self.level) + 'State')(self, self.main_menu)

