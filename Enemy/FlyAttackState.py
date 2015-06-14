from EnemyState import *
from FlyGoBackState import *


class FlyAttackState(EnemyState):

    def __init__(self, enemy):
        super(FlyAttackState, self).__init__(enemy)

    def run(self):
        self.enemy.speed *= 1.5

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

        if self.enemy.left_right:
            self.enemy.xSpeed += self.enemy.speed
        else:
            self.enemy.xSpeed -= self.enemy.speed

        '''
        if self.enemy.block_l or self.enemy.block_r:
            self.enemy.xSpeed = 0
            self.enemy.jump()
        '''

        if not self.enemy.follow:
            self.enemy.states = [FlyGoBackState(self.enemy)]

    def draw(self):
        pass
