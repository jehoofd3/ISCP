from SnakeAttackState import *
from Enemy import *
from Helpers.DatabaseReceiver import *


class Snake(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None
    l_r, OB, LR = None, None, None

    def __init__(self, x, y, range):
        self.w_l = []
        self.w_r = []

        self.w_l.append(DatabaseReceiver.get_enemy_img("Snake", "l_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Snake", "l_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Snake", "r_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Snake", "r_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Snake", "d_l")
        self.d_r = DatabaseReceiver.get_enemy_img("Snake", "d_r")

        self.OB = DatabaseReceiver.get_enemy_img("Snake", "Snake_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Snake", "Snake_LR")
        super(Snake, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [SnakeAttackState(self)]
