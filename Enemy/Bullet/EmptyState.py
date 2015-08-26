from BulletState import *
import pygame
from Helpers.DatabaseReceiver import *


class EmptyState(BulletState):

    def __init__(self, bullet):
        # This game is object oriented and the class extends from BulletState,
        # so its required
        # to call the super class by using the super() method.
        super(EmptyState, self).__init__(bullet)

        # This line of code uses the DatabaseReceiver to change the,
        # image of the bullet.
        self.bullet.img = DatabaseReceiver.get_bullet_img("empty")

    def update(self):
        pass
