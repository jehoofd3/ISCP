import pygame
from Helpers.Artist import *
from FlyNormalState import *
from EnemyDieState import *
from Animation.EnemyAnimation import *


class Enemy(object):
    states = []
    block_u, block_d, block_r, block_l = None, None, None, None
    dead, follow, left_right = False, False, None

    def __init__(self, x, y, range, walk_l, walk_r, dead_l, dead_r):
        self.rect = walk_l[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2
        self.speed = 2
        self.start_speed = self.speed
        self.range = range
        self.start_x = x
        self.start_y = y

        # Player under sprite
        self.enemy_under_image = pygame.sprite.Sprite()
        self.enemy_under_image.image = pygame.image.load("../Data/OB.png").convert()
        self.enemy_under_image.rect = pygame.Rect(0, 0, self.rect.width * 0.8, 1)

        # Player up sprite
        self.enemy_up_image = pygame.sprite.Sprite()
        self.enemy_up_image.image = pygame.image.load("../Data/OB.png").convert()
        self.enemy_up_image.rect = pygame.Rect(0, 0, self.rect.width * 0.8, 1)

        # Player left sprite
        self.enemy_left_image = pygame.sprite.Sprite()
        self.enemy_left_image.image = pygame.image.load("../Data/LR.png").convert()
        self.enemy_left_image.rect = pygame.Rect(0, 0, 1, self.rect.height * 0.8)

        # Player right sprite
        self.enemy_right_image = pygame.sprite.Sprite()
        self.enemy_right_image.image = pygame.image.load("../Data/LR.png").convert()
        self.enemy_right_image.rect = pygame.Rect(0, 0, 1, self.rect.height * 0.8)

        self.animation = EnemyAnimation(walk_l, walk_r, dead_l, dead_r)

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

        # PLayer under
        self.enemy_under_image.rect.x = self.rect.x + 1
        self.enemy_under_image.rect.y = self.rect.y + self.rect.width + 1
        print self.rect.width

        # PLayer up
        self.enemy_up_image.rect.x = self.rect.x
        self.enemy_up_image.rect.y = self.rect.y - 1

        # PLayer left
        self.enemy_left_image.rect.x = self.rect.x - 1
        self.enemy_left_image.rect.y = self.rect.y

        # PLayer right
        self.enemy_right_image.rect.x = self.rect.x + self.rect.width
        self.enemy_right_image.rect.y = self.rect.y

        if self.rect.bottom >= 960:
            self.kill()

    def draw(self):
        Artist.get_display().blit(self.animation.update(self.xSpeed, self.dead), self.rect)
        Artist.get_display().blit(self.enemy_under_image.image, self.enemy_under_image.rect)
        Artist.get_display().blit(self.enemy_up_image.image, self.enemy_up_image.rect)
        Artist.get_display().blit(self.enemy_left_image.image, self.enemy_left_image.rect)
        Artist.get_display().blit(self.enemy_right_image.image, self.enemy_right_image.rect)

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
