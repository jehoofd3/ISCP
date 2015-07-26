from Helpers.Artist import *
from Enemy.Bullet.BulletExplosionState import *
from BulletFollowState import *
from Helpers.DatabaseReceiver import *
import random


class Bullet(object):
    states = []
    img = None

    def __init__(self, x, y, left_right):
        self.img = DatabaseReceiver.get_bullet_img("bullet")
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 0
        self.ySpeed = random.randint(1, 6)
        self.speed = 8
        self.active = True
        self.left_right = left_right

        self.angle = 0
        self.states = [BulletFollowState(self)]

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

        if self.ySpeed > 0:
            self.angle = 360 - self.ySpeed
        else:
            self.angle = self.ySpeed

    def draw(self):
        if self.xSpeed > 0:
            Artist.rotate_img(self.img, self.rect, self.angle)
        else:
            Artist.rotate_img(self.img, self.rect, self.angle + 180)

    def basic_movement(self):
        self.rect.x += self.xSpeed
        self.rect.y -= self.ySpeed
        self.xSpeed = 0

    def gravity(self):
        self.ySpeed -= 0.1

    def explode(self):
        self.states = [BulletExplosionState(self)]

    def move_with_map(self, shift_x):
        self.rect.x -= shift_x
