from PlayerState import *
from Map.TileGrid import *
import pygame
from Helpers.Artist import *

class PlayerNormalState (PlayerState):

    def __init__(self, player):
        super(PlayerNormalState, self).__init__(player)
        self.player = player

    def run(self):
        pass

    def update(self):
        self.player.basic_movement()
        self.player.gravity()

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and not self.player.block_l:
            self.player.xSpeed -= 5

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and not self.player.block_r:
            self.player.xSpeed += 5

        if self.player.block_u:
            self.ySpeed = 0
            self.player.rect.top += 5

        # Collision under
        if self.player.block_d:
            self.player.ySpeed = 0
            self.player.rect.bottom = ((self.player.rect.bottom / 64) * 64)
            self.player.jumpsRemaining = 2


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.player.jumpsRemaining > 0:
                    self.player.jump()

    def draw(self):
        pass
