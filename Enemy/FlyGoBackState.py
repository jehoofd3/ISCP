from EnemyState import *
import FlyNormalState as fn


class FlyGoBackState(EnemyState):

    def __init__(self, enemy):
        super(FlyGoBackState, self).__init__(enemy)

    def run(self):
        self.enemy.speed = self.enemy.start_speed

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

        if self.enemy.rect.x > self.enemy.start_x:
            self.enemy.xSpeed -= self.enemy.speed
        else:
            self.enemy.xSpeed += self.enemy.speed

        if self.enemy.rect.x > self.enemy.start_x - 10 and \
            self.enemy.rect.x < self.enemy.start_x + 10:
            self.enemy.states = [fn.FlyNormalState(self.enemy)]

    def draw(self):
        pass