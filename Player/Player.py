import pygame
from Helpers.Artist import *
from PlayerNormalState import *


class Player (object):
    states = []

    x = 0
    y = 0
    xSpeed = 0
    ySpeed = 0
    jumpsRemaining = 2
    jumpWasPressed = False
    jumpPressed = False
    imagePath = "Test.png"

    def __init__(self, x, y, imagePath):
        self.states = [PlayerNormalState(self)]

        self.x = x
        self.y = y
        self.imagePath = imagePath

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