from abc import ABCMeta, abstractmethod


class EnemyState(object):
    __metaclass__ = ABCMeta

    def __init__(self, enemy):
        self.enemy = enemy
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