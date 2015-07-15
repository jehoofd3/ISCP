from SnakeAttackState import *
from Enemy import *


class Snake(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None
    l_r, OB, LR = None, None, None

    def __init__(self, x, y, range):
        self.w_l = []
        self.w_r = []

        self.w_l.append(pygame.image.load("../Data/Images/Enemy/Snake/l_0.png").convert_alpha())
        self.w_l.append(pygame.image.load("../Data/Images/Enemy/Snake/l_1.png").convert_alpha())
        self.w_r.append(pygame.image.load("../Data/Images/Enemy/Snake/r_0.png").convert_alpha())
        self.w_r.append(pygame.image.load("../Data/Images/Enemy/Snake/r_1.png").convert_alpha())
        self.d_l = pygame.image.load("../Data/Images/Enemy/Snake/d_l.png").convert_alpha()
        self.d_r = pygame.image.load("../Data/Images/Enemy/Snake/d_r.png").convert_alpha()

        self.OB = pygame.image.load("../Data/Images/Enemy/Snake/Snake_OB.png").convert_alpha()
        self.LR = pygame.image.load("../Data/Images/Enemy/Snake/Snake_LR.png").convert_alpha()
        super(Snake, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [SnakeAttackState(self)]
