import time
from BulletState import *


class BulletFollowState(BulletState):

    def __init__(self, bullet):
        super(BulletFollowState, self).__init__(bullet)

    def run(self):
        pass

    def update(self):
        self.bullet.basic_movement()
        self.bullet.gravity()

        if self.bullet.left_right:
            self.bullet.xSpeed -= self.bullet.speed
        else:
            self.bullet.xSpeed += self.bullet.speed

    def draw(self):
        pass