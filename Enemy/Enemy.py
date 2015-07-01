import pygame
from Helpers.Artist import *
from FlyNormalState import *
from EnemyDieState import *
from Animation.EnemyAnimation import *


class Enemy(object):
    states = []
    block_u, block_d, block_r, block_l = None, None, None, None
    dead, follow, left_right = False, False, None

    def __init__(self, x, y, range, walk_l, walk_r, dead_l, dead_r, OB, LR):
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
        self.enemy_under_image.image = OB
        self.enemy_under_image.rect = self.enemy_under_image.image.get_rect()

        # Player up sprite
        self.enemy_up_image = pygame.sprite.Sprite()
        self.enemy_up_image.image = OB
        self.enemy_up_image.rect = self.enemy_up_image.image.get_rect()

        # Player left sprite
        self.enemy_left_image = pygame.sprite.Sprite()
        self.enemy_left_image.image = LR
        self.enemy_left_image.rect = self.enemy_left_image.image.get_rect()

        # Player right sprite
        self.enemy_right_image = pygame.sprite.Sprite()
        self.enemy_right_image.image = LR
        self.enemy_right_image.rect = self.enemy_right_image.image.get_rect()

        self.animation = EnemyAnimation(walk_l, walk_r, dead_l, dead_r)

    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

        # Enemy under
        self.enemy_under_image.rect.x = self.rect.x + 1
        self.enemy_under_image.rect.y = self.rect.y + (self.rect.width/2) + 1


        # Enemy up
        self.enemy_up_image.rect.x = self.rect.x
        self.enemy_up_image.rect.y = self.rect.y - 1

        # Enemy left
        self.enemy_left_image.rect.x = self.rect.x - 1
        self.enemy_left_image.rect.y = self.rect.y

        # Enemy right
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
