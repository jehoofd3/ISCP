from PlayerState import *
from Map.TileGrid import *
import pygame
from Helpers.Artist import *


class PlayerNormalState (PlayerState):

    player_standard_speed = 6
    player_x_speed = 6
    half_screen_width = Artist.get_half_screen_width()

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

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and not self.player.block_l:
            self.player.xSpeed -= self.player_x_speed

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and not self.player.block_r:
            self.player.xSpeed += self.player_x_speed

        if self.player.block_u:
            self.player.ySpeed = 0
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

        # zodat de player x speed door de helft gaat als de map meegaat
        if self.player.rect.x >= self.half_screen_width:
            self.player_x_speed = self.player_standard_speed / 2
        else:
            self.player_x_speed = self.player_standard_speed

    def draw(self):
        pass
