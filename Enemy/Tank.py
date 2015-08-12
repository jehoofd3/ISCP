from Enemy import *
from TankNormalState import *
from TankShootState import *
from Helpers.Artist import *
from Bullet.Bullet import *
from Helpers.Artist import *
from Player.Player import *
from Helpers.DatabaseReceiver import *


class Tank(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None
    OB, LR = None, None

    def __init__(self, x, y, range):
        self.w_l = []
        self.w_r = []

        self.w_l.append(DatabaseReceiver.get_enemy_img("Tank", "l_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Tank", "l_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Tank", "r_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Tank", "r_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Tank", "d_l")
        self.d_r = DatabaseReceiver.get_enemy_img("Tank", "d_r")

        self.OB = DatabaseReceiver.get_enemy_img("Tank", "Tank_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Tank", "Tank_LR")

        super(Tank, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [TankNormalState(self)]

    def update(self):
        super(Tank, self).update()

        for b in self.bullet_list:
            b.update()

    def draw(self):
        super(Tank, self).draw()

        for b in self.bullet_list:
            b.draw()

    def add_bullet(self, x, y, left_right):
        self.bullet_list.append(Bullet(x, y, left_right))

    def get_bl(self):
        return self.bullet_list
