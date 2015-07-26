from BulletState import *
import pygame
import time
from Helpers.DatabaseReceiver import *
from EmptyState import *


class BulletExplosionState(BulletState):

    def __init__(self, bullet):
        super(BulletExplosionState, self).__init__(bullet)

        self.bullet.img = DatabaseReceiver.get_bullet_img("smokeWhite3")
        self.start_time = time.time()
        self.del_time = 2
        self.bullet.active = False

    def run(self):
        pass

    def update(self):
        if time.time() - self.start_time >= self.del_time:
            self.bullet.states = [EmptyState(self.bullet)]

    def draw(self):
        pass
