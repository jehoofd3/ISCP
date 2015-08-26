from abc import ABCMeta, abstractmethod


# This abstract class is needed for the state machine.
class BulletState(object):
    # This module provides the infrastructure for defining,
    # abstract base classes (ABCs).
    __metaclass__ = ABCMeta

    # This constructor needs an Bullet object.
    def __init__(self, bullet):
        self.bullet = bullet

    # This line of code is a decorator indicating,
    # abstract methods.
    # The states overload this method.
    @abstractmethod
    def update(self):
        pass
