from Enemy import *
from SlimeNormalState import *
from Snake import *


class Slime(Enemy):
    w_l, w_r, d_l, d_r = [None, None], [None, None], None, None
    snake_list = []

    def __init__(self, x, y, range):
        self.w_l[0] = (pygame.image.load("../Data/Images/Enemy/Slime/slime_0.png").convert_alpha())
        self.w_l[1] = (pygame.image.load("../Data/Images/Enemy/Slime/slime_1.png").convert_alpha())
        self.w_r[0] = (pygame.image.load("../Data/Images/Enemy/Slime/slime_0.png").convert_alpha())
        self.w_r[1] = (pygame.image.load("../Data/Images/Enemy/Slime/slime_1.png").convert_alpha())
        self.d_l = pygame.image.load("../Data/Images/Enemy/Slime/slime_d.png").convert_alpha()
        self.d_r = pygame.image.load("../Data/Images/Enemy/Slime/slime_d.png").convert_alpha()

        self.OB = pygame.image.load("../Data/Images/Enemy/Slime/Slime_OB.png").convert()
        self.LR = pygame.image.load("../Data/Images/Enemy/Slime/Slime_LR.png").convert()
        super(Slime, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l, self.d_r, self.OB, self.LR)

        self.states = [SlimeNormalState(self)]

    def update(self):
        self.states[0].update()
        for snake in self.snake_list:
            snake.update()

    def draw(self):
        Artist.get_display().blit(self.animation.update(self.xSpeed, self.dead), self.rect)
        for i in range(len(self.snake_list)):
            self.snake_list[i].draw()

    def add_snake(self, x, y):
        self.snake_list.append(Snake(x, y, 0))

    def get_snake(self, index):
        return self.snake_list[index]
