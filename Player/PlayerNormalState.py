from PlayerState import *
import pygame
from Helpers.Artist import *

class PlayerNormalState (PlayerState):

    def __init__(self, player):
        super(PlayerNormalState, self).__init__(player)
        self.player = player

    def run(self):
        pass

    def update(self):
        self.player.x += self.player.xSpeed
        self.player.y -= self.player.ySpeed

        self.player.xSpeed = 0

        self.player.ySpeed -= 0.4

        if(self.player.y >= 786 - 100):
            self.player.ySpeed = 0
            self.player.jumpsRemaining = 2

        if(pygame.key.get_pressed() [pygame.K_LEFT] != 0):
            self.player.xSpeed -= 5

        if(pygame.key.get_pressed() [pygame.K_RIGHT] != 0):
            self.player.xSpeed += 5

        for event in pygame.event.get():
            if event.type == pygame.K_UP:
                self.player.jump()

    def draw(self):
        Artist.draw_textures(self.player.image, self.player.x, self.player.y)