from GameStateManager import *
from abc import ABCMeta, abstractmethod


class GameState(object):
    __metaclass__ = ABCMeta



    def __init__(self, gsm):
        self.gsm = gsm
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