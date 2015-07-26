from FlyNormalState import *
from Enemy import *
from Helpers.DatabaseReceiver import *



class Fly(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None

    def __init__(self, x, y, range):
        self.w_l = []
        self.w_r = []

        self.w_l.append(DatabaseReceiver.get_enemy_img("Fly", "l_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Fly", "l_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Fly", "r_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Fly", "r_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Fly", "d_l")
        self.d_r = DatabaseReceiver.get_enemy_img("Fly", "d_r")

        self.OB = DatabaseReceiver.get_enemy_img("Fly", "Fly_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Fly", "Fly_LR")
        super(Fly, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [FlyNormalState(self)]
