import pygame
from Helpers.Artist import *
from FlyNormalState import *
from Sprite.SpriteSheet import *
from EnemyDieState import *
from Animation.EnemyAnimation import *


class Enemy(object):
    states, walk_l, walk_r = [], [], []
    dead_l, dead_r = None, None
    block_u, block_d, block_r, block_l = None, None, None, None
    dead = False

    def __init__(self, x, y):
        self.image = pygame.image.load("../Data/Images/Enemy/Fly/l_0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2

    def run(self):
        self.animation = EnemyAnimation(self)
        self.states[0].run()

    def update(self):
        self.states[0].update()
        self.image = self.animation.update()

    def draw(self):
        Artist.get_display().blit(self.animation.update(), self.rect)

    def jump(self):
        self.ySpeed += 10
        self.jumpsRemaining -= 1

    def basic_movement(self):
        self.rect.x += self.xSpeed
        self.rect.y -= self.ySpeed
        self.xSpeed = 0

    def gravity(self):
        self.ySpeed -= 0.4

    def kill(self):
        self.states.pop()
        self.states = [EnemyDieState(self)]
