from EnemyState import *


class EnemyDieState(EnemyState):

    def __init__(self, enemy):
        super(EnemyDieState, self).__init__(enemy)
        self.enemy = enemy

    def run(self):
        self.enemy.dead = True

    def update(self):
        pass

    def draw(self):
        pass