import pygame
from Helpers.Artist import *
from FlyNormalState import *
from Sprite.SpriteSheet import *
from EnemyDieState import *
from Animation.EnemyAnimation import *


class Enemy(object):
    states = []
    block_u, block_d, block_r, block_l = None, None, None, None
    dead, follow, left_right = False, False, None

    def __init__(self, x, y, range, walk_l, walk_r, dead_l, dead_r):
        self.image = pygame.image.load("../Data/Images/Enemy/Fly/l_0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2
        self.speed = 2
        self.start_speed = 2
        self.range = range

        self.animation = EnemyAnimation(walk_l, walk_r, dead_l, dead_r)

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        Artist.get_display().blit(self.animation.update(self.xSpeed, self.dead), self.rect)

    def jump(self):
        if self.jumpsRemaining > 0:
            self.ySpeed += 10
            self.jumpsRemaining -= 1

    def basic_movement(self):
        self.rect.x += self.xSpeed
        self.rect.y -= self.ySpeed
        self.xSpeed = 0

    def gravity(self):
        self.ySpeed -= 0.4

    def kill(self):
        self.states = [EnemyDieState(self)]

    def reset_images(self):
        self.walk_l = []
        self.walk_r = []
        self.dead_l = None
        self.dead_r = None
