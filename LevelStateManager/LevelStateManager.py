from MainMenu.MainMenu import *
from Level2State import *
from Level3State import *
from EndDemo import *
from Timer import *
import sys

class LevelStateManager(object):

    states = None
    level_state = None
    level = 1
    main_menu = None
    player_health = 3

    def __init__(self):
        self.states = MainMenu(self)
        self.main_menu = self.states
        self.states.run()

    def run(self):
        self.states.run()

    def update(self):
        self.states.update()

        if not isinstance(self.states, MainMenu):
            for event in pygame.event.get(pygame.KEYDOWN):
                if event.key == pygame.K_e:
                    self.next_level()
                if event.key == pygame.K_r:
                    self.states.reset_best_time()

    def draw(self):
        self.states.draw()

    def next_level(self):
        self.states.timer.save_best_time(self.level)
        self.level += 1

        if self.level == 5:
            self.states = EndDemo()
            self.states.run()
        else:
            self.states = getattr(sys.modules[__name__], 'Level' + str(self.level) + 'State')(self, self.main_menu)
            self.states.run()

    def reset_level(self):
        self.states = getattr(sys.modules[__name__], 'Level' + str(self.level) + 'State')(self, self.main_menu)
        self.states.run()

    def open_level1(self):
        self.level = 1
        self.states = Level1State(self, self.main_menu)
        self.states.run()

