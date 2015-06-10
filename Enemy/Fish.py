from Enemy import *


class Fish(Enemy):

    def __init__(self, x, y):
        super(Fish, self).__init__(self, x, y)

        self.walk_l.append(pygame.image.load("../Data/Images/Enemy/Fish/l_0.png").convert_alpha())
        self.walk_l.append(pygame.image.load("../Data/Images/Enemy/Fish/l_1.png").convert_alpha())
        self.walk_r.append(pygame.image.load("../Data/Images/Enemy/Fish/r_0.png").convert_alpha())
        self.walk_r.append(pygame.image.load("../Data/Images/Enemy/Fish/r_1.png").convert_alpha())
        self.dead_l = pygame.image.load("../Data/Images/Enemy/Fish/d_l.png").convert_alpha()
        self.dead_r = pygame.image.load("../Data/Images/Enemy/Fish/d_r.png").convert_alpha()

        self.states = []
        self.run()
