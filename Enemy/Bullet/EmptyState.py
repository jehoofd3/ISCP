from BulletState import *
import pygame


class EmptyState(BulletState):

    def __init__(self, bullet):
        super(EmptyState, self).__init__(bullet)

    def run(self):
        self.bullet.img = pygame.image.load("../Data/Images/Enemy/Tank/Tank_OB.png").convert_alpha()

    def update(self):
        pass

    def draw(self):
        pass