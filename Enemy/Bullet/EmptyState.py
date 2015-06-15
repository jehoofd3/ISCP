from BulletState import *
import pygame


class EmptyState(BulletState):

    def __init__(self, bullet):
        super(EmptyState, self).__init__(bullet)

    def run(self):
        self.bullet.active = False
        self.bullet.b_l = pygame.image.load("../Data/Images/Bullet/Smoke/empty.png").convert_alpha()
        self.bullet.b_r = pygame.image.load("../Data/Images/Bullet/Smoke/empty.png").convert_alpha()

    def update(self):
        pass

    def draw(self):
        pass