from EnemyState import *
from TankShootState import *


class TankNormalState(EnemyState):

    def __init__(self, enemy):
        super(TankNormalState, self).__init__(enemy)

    def run(self):
        self.right = None
        self.left = None
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

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

        if self.enemy.block_l:
            self.enemy.xSpeed = 0
            self.enemy.rect.x += 1

        if  self.enemy.block_r:
            self.enemy.xSpeed = 0
            self.enemy.rect.x -= 1

        if self.left:
            self.enemy.xSpeed -= self.enemy.speed
        if self.right:
            self.enemy.xSpeed += self.enemy.speed

        if self.enemy.follow:
            self.enemy.states = [TankShootState(self.enemy)]


    def draw(self):
        pass