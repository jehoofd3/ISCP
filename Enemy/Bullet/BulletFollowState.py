import time
from BulletState import *


class BulletFollowState(BulletState):

    def __init__(self, bullet):
        # This game is object oriented and the class extends from BulletState,
        # so its required
        # to call the super class by using the super() method.
        super(BulletFollowState, self).__init__(bullet)

    def update(self):
        # The state called the basic_movement and gravity method,
        # so it can move on both axis.
        self.bullet.basic_movement()
        self.bullet.gravity()

        # When the variable left_right is True, add the speed to the value of,
        # the bullets x position.
        # This code lets the bullet move left or right.
        if self.bullet.left_right:
            self.bullet.x_speed -= self.bullet.speed
        else:
            self.bullet.x_speed += self.bullet.speed

    def draw(self):
        pass

