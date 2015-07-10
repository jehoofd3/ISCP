from BulletState import *
import pygame
import time
from EmptyState import *


class BulletExplosionState(BulletState):

    def __init__(self, bullet):
        super(BulletExplosionState, self).__init__(bullet)

    def run(self):
        self.bullet.img = pygame.image.load("../Data/Images/Bullet/Smoke/smokeWhite3.png").convert_alpha()
        self.start_time = time.time()
        self.del_time = 2
        self.bullet.active = False

    def update(self):
        if time.time() - self.start_time >= self.del_time:
            self.bullet.states = [EmptyState(self.bullet)]

    def draw(self):
        pass
