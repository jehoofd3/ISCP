from abc import ABCMeta, abstractmethod


class LevelState(object):
    # This class is the superclass of
    # all levels that belong to the LevelStateManager.
    #
    # These are the following levels: MainMenu, OptionsMenu,
    # Level1State, Level2State, Level3State, Level4State, EndDemo.
    #
    # The purpose of this class is so that the levels must contain
    # the abstract methods. (run, update, draw method)
    # It uses the abc library to use the abstractmethod annotation.
    __metaclass__ = ABCMeta

    def __init__(self, level):
        self.level = level
        self.run()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
