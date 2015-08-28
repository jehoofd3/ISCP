from abc import ABCMeta, abstractmethod


# This abstract class is needed for the state machine.
class PlayerState(object):
    # This module provides the infrastructure for defining
    # abstract base classes (ABCs).
    __metaclass__ = ABCMeta

    # This constructor needs an Player object.
    # The states can use the player
    def __init__(self, player):
        self.player = player
        self.run()

    # This line of code is a decorator indicating
    # abstract methods.
    # The states overload this method.
    @abstractmethod
    def run(self):
        pass

    # This line of code is a decorator indicating
    # abstract methods.
    # The states overload this method.
    @abstractmethod
    def update(self):
        pass
