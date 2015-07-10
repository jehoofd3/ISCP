from Helpers.Artist import *
from Enemy.Bullet.BulletExplosionState import *
from BulletFollowState import *


class Bullet(object):
    states = []
    img = None

    def __init__(self, x, y, left_right):
        self.img = pygame.image.load("../Data/Images/Bullet/bullet.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.speed = 8
        self.active = True
        self.left_right = left_right

        self.states = [BulletFollowState(self)]

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        if self.xSpeed > 0:
            Artist.rotate_img(self.img, self.rect, 0)
        else:
            Artist.rotate_img(self.img, self.rect, 180)

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
