from BulletState import *
import pygame


class EmptyState(BulletState):

    def __init__(self, bullet):
        super(EmptyState, self).__init__(bullet)

        self.bullet.img = pygame.image.load("../Data/Images/Bullet/Smoke/empty.png").convert_alpha()

    def run(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass