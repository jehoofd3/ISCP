from abc import ABCMeta, abstractmethod


class LevelState(object):
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
