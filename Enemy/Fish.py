from FishNormalState import *
from Enemy import *
from Helpers.DatabaseReceiver import *


class Fish(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None

    def __init__(self, x, y, range, type):
        self.w_l = []
        self.w_r = []

        self.OB = DatabaseReceiver.get_enemy_img("Fish", "Fish_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Fish", "Fish_LR")

        if type == "Water":
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish", "water_l_0"))
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish", "water_l_1"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish", "water_r_0"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish", "water_r_1"))
            self.d_l = DatabaseReceiver.get_enemy_img("Fish", "water_d_l")
            self.d_r = DatabaseReceiver.get_enemy_img("Fish", "water_d_r")
        else:
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish", "lava_l_0"))
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish", "lava_l_1"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish", "lava_r_0"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish", "lava_r_1"))
            self.d_l = DatabaseReceiver.get_enemy_img("Fish", "lava_d_l")
            self.d_r = DatabaseReceiver.get_enemy_img("Fish", "lava_d_r")

        super(Fish, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [FishNormalState(self)]
