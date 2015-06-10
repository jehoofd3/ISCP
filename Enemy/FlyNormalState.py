from EnemyState import *


class FlyNormalState(EnemyState):

    def __init__(self, enemy):
        super(FlyNormalState, self).__init__(enemy)

    def run(self):
        pass

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()

        self.enemy.xSpeed = 3

    def draw(self):
        pass