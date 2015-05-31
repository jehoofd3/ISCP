from GameStateManager import *
from abc import ABCMeta, abstractmethod


class PlayerState(object):
    __metaclass__ = ABCMeta

    def __init__(self, player):
        self.player = player
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