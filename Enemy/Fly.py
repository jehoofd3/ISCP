from FlyNormalState import *
from Enemy import *



class Fly(Enemy):
    w_l, w_r, d_l, d_r = [], [], None, None

    def __init__(self, x, y, range):
        self.w_l = []
        self.w_r = []

        self.w_l.append(pygame.image.load("../Data/Images/Enemy/Fly/l_0.png").convert_alpha())
        self.w_l.append(pygame.image.load("../Data/Images/Enemy/Fly/l_1.png").convert_alpha())
        self.w_r.append(pygame.image.load("../Data/Images/Enemy/Fly/r_0.png").convert_alpha())
        self.w_r.append(pygame.image.load("../Data/Images/Enemy/Fly/r_1.png").convert_alpha())
        self.d_l = pygame.image.load("../Data/Images/Enemy/Fly/d_l.png").convert_alpha()
        self.d_r = pygame.image.load("../Data/Images/Enemy/Fly/d_r.png").convert_alpha()

        self.OB = pygame.image.load("../Data/Images/Enemy/Fly/Fly_OB.png").convert()
        self.LR = pygame.image.load("../Data/Images/Enemy/Fly/Fly_LR.png").convert()
        super(Fly, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [FlyNormalState(self)]
