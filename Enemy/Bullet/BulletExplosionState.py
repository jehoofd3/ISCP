from BulletState import *
import pygame
import time
from Helpers.DatabaseReceiver import *
from EmptyState import *


class BulletExplosionState(BulletState):

    def __init__(self, bullet):
        # This game is object oriented and the class extends from BulletState,
        # so its required
        # to call the super class by using the super() method.
        super(BulletExplosionState, self).__init__(bullet)

        # This line of code uses the DatabaseReceiver to change the,
        # image of the bullet.
        self.bullet.img = DatabaseReceiver.get_bullet_img("smokeWhite3")

        # This variable is the start time of the frame,
        # because it is created in the init it only runs on creation,
        # of this state.
        # It is used to switch to the EmptyState.
        self.start_time = time.time()

        # This variable is used to set the amount of seconds to switch,
        # to the EmptyState.
        self.del_time = 2

        # This variable tells the collider that there is no colission,
        # with this object possible.
        self.bullet.active = False

    def update(self):

        # This method checks if the two seconds are over to switch to,
        # the EmptyState.
        # The time.time() method gets the current time.
        # If this float minus the variable start_time is greater or equal,
        # than del_time it start the EmptyState.
        if time.time() - self.start_time >= self.del_time:
            self.bullet.states = EmptyState(self.bullet)
