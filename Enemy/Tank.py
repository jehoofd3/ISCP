from Enemy import *
from TankNormalState import *
from TankShootState import *
from Helpers.Artist import *
from Bullet.Bullet import *
from Helpers.Artist import *


class Tank(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None
    bullet_list, OB, LR = [], None, None

    def __init__(self, x, y, range):
        self.w_l.append(pygame.image.load("../Data/Images/Enemy/Tank/l_0.png").convert_alpha())
        self.w_l.append(pygame.image.load("../Data/Images/Enemy/Tank/l_1.png").convert_alpha())
        self.w_r.append(pygame.image.load("../Data/Images/Enemy/Tank/r_0.png").convert_alpha())
        self.w_r.append(pygame.image.load("../Data/Images/Enemy/Tank/r_1.png").convert_alpha())
        self.d_l = pygame.image.load("../Data/Images/Enemy/Tank/d_l.png").convert_alpha()
        self.d_r = pygame.image.load("../Data/Images/Enemy/Tank/d_r.png").convert_alpha()

        self.OB = pygame.image.load("../Data/Images/Enemy/Tank/Tank_OB.png").convert()
        self.LR = pygame.image.load("../Data/Images/Enemy/Tank/Tank_LR.png").convert()

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

    def add_bullet(self, x, y):
        self.bullet_list.append(Bullet(x, y, Artist.get_bi()))

    def get_bl(self):
        return self.bullet_list
