import pygame
from Helpers.Artist import *
from PlayerNormalState import *


class Player (object):
    states = []

    def __init__(self, x, y, imagePath):
        self.states = [PlayerNormalState(self)]

        self.image = pygame.image.load(imagePath).convert_alpha()
        self.x = x
        self.y = y

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
        self.states[0].draw()

    def jump(self):
        self.ySpeed += 10
        self.jumpsRemaining -= 1

    def gravity(self):
        pass