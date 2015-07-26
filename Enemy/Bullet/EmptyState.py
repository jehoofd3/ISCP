from BulletState import *
import pygame
from Helpers.DatabaseReceiver import *


class EmptyState(BulletState):

    def __init__(self, bullet):
        super(EmptyState, self).__init__(bullet)

        self.bullet.img = DatabaseReceiver.get_bullet_img("empty")

    def run(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass