import pygame
from PlayerState import *
from Map.TileGrid import *
from Helpers.Artist import *


class PlayerNormalState (PlayerState):

    player_x_speed = 4
    player = None

    def __init__(self, player):
        super(PlayerNormalState, self).__init__(player)
        self.player = player

    def run(self):
        self.player.dead = False
        self.player.rect.x = self.player.start_x
        self.player.rect.y = self.player.start_y
        self.player.ySpeed = 0

    def update(self):
        self.player.basic_movement()
        self.player.gravity()

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and not self.player.canGoLeft:
            self.player.xSpeed = -self.player_x_speed

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and not self.player.canGoRight:
            self.player.xSpeed = self.player_x_speed

        if self.player.player_on_ice:
            self.player.xSpeed = self.player_x_speed

        if self.player.collision_up:
            self.player.ySpeed = - 3

        # Collision under
        if self.player.collision_under:
            self.player.ySpeed = 0
            self.player.rect.bottom = ((self.player.rect.bottom / 64) * 64)
            self.player.jumpsRemaining = 2

        if pygame.key.get_pressed()[pygame.K_UP] and self.player.jumpsRemaining > 0:
            self.player.jump()
            self.player.canGoLeft = True
            self.player.canGoRight = True

    def draw(self):
        pass
