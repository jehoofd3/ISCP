from BulletState import *
import pygame
import time
import EmptyState as es


class BulletExplosionState(BulletState):

    def __init__(self, bullet):
        super(BulletExplosionState, self).__init__(bullet)

    def run(self):
        self.bullet.b_l = pygame.image.load("../Data/Images/Bullet/Smoke/smokeWhite3.png").convert_alpha()
        self.bullet.b_r = pygame.image.load("../Data/Images/Bullet/Smoke/smokeWhite3.png").convert_alpha()
        self.start_time = time.time()
        self.del_time = 1
        self.bullet.active = False

    def update(self):
        if time.time() - self.start_time + self.del_time >= 2:
            self.bullet.states = [es.EmptyState(self.bullet)]

    def draw(self):
        pass
