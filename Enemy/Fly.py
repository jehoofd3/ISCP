from FlyNormalState import *
from Enemy import *


class Fly(Enemy):

    def __init__(self, x, y):
        super(Fly, self).__init__(x, y)

        self.walk_l.append(pygame.image.load("../Data/Images/Enemy/Fly/l_0.png").convert_alpha())
        self.walk_l.append(pygame.image.load("../Data/Images/Enemy/Fly/l_1.png").convert_alpha())
        self.walk_r.append(pygame.image.load("../Data/Images/Enemy/Fly/r_0.png").convert_alpha())
        self.walk_r.append(pygame.image.load("../Data/Images/Enemy/Fly/r_1.png").convert_alpha())
        self.dead_l = pygame.image.load("../Data/Images/Enemy/Fly/d_l.png").convert_alpha()
        self.dead_r = pygame.image.load("../Data/Images/Enemy/Fly/d_r.png").convert_alpha()

        self.states = [FlyNormalState(self)]
        self.run()
