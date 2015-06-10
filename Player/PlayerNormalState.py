from PlayerState import *
from Map.TileGrid import *
import pygame
from Helpers.Artist import *

class PlayerNormalState (PlayerState):

    def __init__(self, player):
        super(PlayerNormalState, self).__init__(player)
        self.player = player
        self.block_u, self.block_d, self.block_r, self.block_l = None, None, None, None

    def run(self):
        pass

    def update(self):
        self.player.basic_movement()
        self.player.gravity()

        blocks_hit_list = pygame.sprite.spritecollide(self.player, TileGrid.get_group(), False)
        for block in blocks_hit_list:

            # Collision up
            if (self.player.rect.top <= block.rect.bottom and self.player.rect.top >= block.rect.top):
                self.block_u = True
            else:
                self.block_u = False

            # Collision under
            if (self.player.rect.bottom >= block.rect.top and self.player.rect.bottom <= block.rect.bottom):
                self.block_d = True
            else:
                self.block_d = False

            # Collision right
            if (self.player.rect.right >= block.rect.left and self.player.rect.right <= block.rect.right and
                self.player.rect.bottom <= block.rect.bottom):
                self.block_r = True
            else:
                self.block_r = False

            #Collision left
            if (self.player.rect.left <= block.rect.right and self.player.rect.left >= block.rect.left and
                self.player.rect.bottom <= block.rect.bottom):
                self.block_l = True
            else:
                self.block_l = False

        # Als de list leeg is, betekend het dat de player geen collision met Tile(s) heeft. Door alle variablen op False
        # te zetten blijft de Gravity actief en kan de player naar links / rechts bewegen en springen
        if not blocks_hit_list:
            self.block_u = False
            self.block_d = False
            self.block_l = False
            self.block_r = False

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0 and not self.block_l:
            self.player.xSpeed -= 5

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and not self.block_r:
            self.player.xSpeed += 5

        if self.block_u:
            self.ySpeed = 0
            self.player.rect.top += 5

        # Collision under
        if self.block_d:
            self.player.ySpeed = 0
            self.player.rect.bottom = ((self.player.rect.bottom / 64) * 64)
            self.player.jumpsRemaining = 2


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.player.jumpsRemaining > 0:
                    self.player.jump()

    def draw(self):
        pass
