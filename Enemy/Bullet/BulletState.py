from abc import ABCMeta, abstractmethod


class BulletState(object):
    __metaclass__ = ABCMeta

    def __init__(self, bullet):
        self.bullet = bullet
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