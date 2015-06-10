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

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

    def draw(self):
        pass