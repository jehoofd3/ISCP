from Enemy import *
from SlimeNormalState import *
from Snake import *


class Slime(Enemy):
    w_l, w_r, d_l, d_r = [None, None], [None, None], None, None
    snake_list = []
    snake_hulp = 0

    def __init__(self, x, y):
        self.snake_list = []
        self.snake_hulp = 0
        self.w_l = []
        self.w_r = []

        self.w_l.append(DatabaseReceiver.get_enemy_img("Slime", "slime_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Slime", "slime_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Slime", "slime_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Slime", "slime_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Slime", "slime_d")

        self.OB = DatabaseReceiver.get_enemy_img("Slime", "Slime_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Slime", "Slime_LR")
        super(Slime, self).__init__(x, y, 0, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [SlimeNormalState(self)]

    def add_snake(self, x, y):
        self.snake_list.append(Snake(x, y, 0))

    def get_snake(self, index):
        return self.snake_list[index]
