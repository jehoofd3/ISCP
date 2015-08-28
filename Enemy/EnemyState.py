from abc import ABCMeta, abstractmethod


# This abstract class is needed for the state machine.
class EnemyState(object):
    # This module provides the infrastructure for defining
    # abstract base classes (ABCs).
    __metaclass__ = ABCMeta

    # This constructor needs an Enemy object.
    # The states can use the enemy
    def __init__(self, enemy):
        self.enemy = enemy

    # This line of code is a decorator indicating
    # abstract methods.
    # The states overload this method.
    @abstractmethod
    def update(self):
        pass
