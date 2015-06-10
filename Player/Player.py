import pygame
from Helpers.Artist import *
from PlayerNormalState import *
from Animation.PlayerAnimation import *


class Player (pygame.sprite.Sprite):
    states, walk_l, walk_r = [], [], []
    dead_l, dead_r, jump_l, jump_r, stand_l, stand_r = None, None, None, None, None, None
    block_u, block_d, block_r, block_l = None, None, None, None

    def __init__(self, x, y):
        self.states = [PlayerNormalState(self)]

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../Data/Images/Player/stand_r.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2
        self.jumpWasPressed = None
        self.jumpPressed = None

        for i in range(11):
            self.walk_l.append(pygame.image.load("../Data/Images/Player/Left/l_" + str(i) + ".png").convert_alpha())

        for i in range(11):
            self.walk_r.append(pygame.image.load("../Data/Images/Player/Right/r_" + str(i) + ".png").convert_alpha())

        self.jump_r = pygame.image.load("../Data/Images/Player/jump_r.png").convert_alpha()
        self.jump_l = pygame.image.load("../Data/Images/Player/jump_l.png").convert_alpha()
        self.dead_l = pygame.image.load("../Data/Images/Player/dead_l.png").convert_alpha()
        self.dead_r = pygame.image.load("../Data/Images/Player/dead_r.png").convert_alpha()
        self.stand_l = pygame.image.load("../Data/Images/Player/stand_l.png").convert_alpha()
        self.stand_r = pygame.image.load("../Data/Images/Player/stand_r.png").convert_alpha()
        self.animation = PlayerAnimation(self)



    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        Artist.get_display().blit(self.animation.update(), self.rect)

    def jump(self):
        self.ySpeed = 10
        self.jumpsRemaining -= 1

    def basic_movement(self):
        self.rect.x += self.xSpeed
        self.rect.y -= self.ySpeed
        self.xSpeed = 0

    def gravity(self):
        self.ySpeed -= 0.4

    def kill(self):
        self.states[0] = [PlayerDieState(self)]
