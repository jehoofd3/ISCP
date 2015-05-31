import pygame
from Helpers.Artist import *
from PlayerNormalState import *


class Player (pygame.sprite.Sprite):
    states = []

    walk_l = []
    walk_r = []

    def __init__(self, x, y, image):
        # image kan uit de constructor zodat we in de constructor de sprite
        # kunnen laden en daar de l en r images uit kunnen halen

        self.states = [PlayerNormalState(self)]
        self.player_group = pygame.sprite.Group()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player_group.add(self)

        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2
        self.jumpWasPressed = False
        self.jumpPressed = False



    def run(self):
        self.states[0].run()

    def update(self):
        self.states[0].update()

    def draw(self):
        self.player_group.draw(Artist.get_display())

    def jump(self):
        self.ySpeed += 10
        self.jumpsRemaining -= 1

    def gravity(self):
        pass

    def get_group(self):
        return self.player_group