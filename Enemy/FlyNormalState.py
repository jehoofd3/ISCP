from EnemyState import *
from FlyAttackState import *


class FlyNormalState(EnemyState):

    def __init__(self, enemy):
        super(FlyNormalState, self).__init__(enemy)

    def run(self):
        self.right = True
        self.left = False
        self.enemy.speed = self.enemy.start_speed

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()

        if self.enemy.rect.x <= self.enemy.start_x:
            self.right = True
            self.left = False

        if self.enemy.rect.x > self.enemy.start_x + self.enemy.range:
            self.right = False
            self.left = True

        if self.left:
            self.enemy.xSpeed -= self.enemy.speed
        if self.right:
            self.enemy.xSpeed += self.enemy.speed

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

        if self.enemy.block_l or self.enemy.block_r:
            self.enemy.xSpeed = 0

        if self.enemy.follow:
            self.enemy.states = [FlyAttackState(self.enemy)]

        self.draw()

    def draw(self):
        pass
