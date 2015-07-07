import time
from BulletState import *


class BulletFollowState(BulletState):

    def __init__(self, bullet):
        super(BulletFollowState, self).__init__(bullet)

    def run(self):
        self.start_time = time.time()
        self.switch_time = 7

    def update(self):
        self.bullet.basic_movement()
        if self.bullet.l_r:
            self.bullet.xSpeed -= self.bullet.speed
        else:
            self.bullet.xSpeed += self.bullet.speed

        if self.bullet.u_d:
            self.bullet.ySpeed += self.bullet.speed
        else:
            self.bullet.ySpeed -= self.bullet.speed

        if time.time() - self.start_time >= self.switch_time:
            self.bullet.explode()

    def draw(self):
        pass