from Helpers.Artist import *
from Enemy.Bullet.BulletExplosionState import *
from BulletFollowState import *


class Bullet(object):
    states = []
    l_r, u_d = None, None

    def __init__(self, x, y, index):
        self.b_l = pygame.image.load("../Data/Images/Bullet/b_l.png").convert_alpha()
        self.b_r = pygame.image.load("../Data/Images/Bullet/b_r.png").convert_alpha()
        self.rect = self.b_l.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.speed = 2
        self.active = True

        self.index = index

        self.states = [BulletFollowState(self)]

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        if self.xSpeed > 0:
            Artist.get_display().blit(self.b_r, self.rect)
        else:
            Artist.get_display().blit(self.b_l, self.rect)

    def basic_movement(self):
        self.rect.x += self.xSpeed
        self.rect.y -= self.ySpeed
        self.xSpeed = 0
        self.ySpeed = 0

    def explode(self):
        self.states = [BulletExplosionState(self)]
