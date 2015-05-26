import pygame
from Helpers.Artist import *


class Player (object):

    width = 0
    height = 0
    x = 0
    y = 0
    xSpeed = 0
    ySpeed = 0
    jumpsRemaining = 2
    jumpWasPressed = False
    jumpPressed = False
    imagePath = "Test.png"

    def __init__(self, width, height, x, y, imagePath):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imagePath = imagePath

    def update(self):

        self.x += self.xSpeed
        self.y -= self.ySpeed

        self.xSpeed = 0

        self.ySpeed -= 0.4

        if(self.y >= 786 - 100):
            self.ySpeed = 0
            self.jumpsRemaining = 2

        if(pygame.key.get_pressed() [pygame.K_LEFT] != 0):
            self.xSpeed -= 5

        if(pygame.key.get_pressed() [pygame.K_RIGHT] != 0):
            self.xSpeed += 5

        for event in pygame.event.get():
            if event.type == pygame.K_UP:
                self.jump()

    def draw(self):
        drawTextures(self.imagePath, self.x, self.y, self.width, self.height)

    def jump(self):
        self.ySpeed += 10
        self.jumpsRemaining -= 1