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

        self.states = [TankShootState(self)]

    def update(self):
        self.states[0].update()
        for i in range(len(self.bullet_list)):
            self.bullet_list[i].update()

    def draw(self):
        Artist.get_display().blit(self.animation.update(self.xSpeed, self.dead), self.rect)

        for i in range(len(self.bullet_list)):
            self.bullet_list[i].draw()

    def add_bullet(self, x, y):
        self.bullet_list.append(Bullet(x, y, Artist.get_bi()))

    def get_bl(self):
        return self.bullet_list

    def get_len_bl(self):
        return len(self.bullet_list)
