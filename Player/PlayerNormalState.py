import pygame
from Helpers.Artist import *
from Map.TileGrid import *


class PlayerNormalState:

    walk_l = []
    walk_r = []

    block_u = False
    block_d = False
    block_l = False
    block_r = False

    tile_length = 64


    spawn_x = 500
    spawn_y = 10
    image_player = "../Data/Images/p2_front.png"

    player = pygame.sprite.Sprite()

    gravity = 0.4

    def __init__(self):
        self.player.image = pygame.image.load(self.image_player).convert_alpha()
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = self.spawn_x
        self.player.rect.y = self.spawn_y
        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2

    def run(self):
        pass

    def update(self):

        self.player.rect.x += self.xSpeed
        self.player.rect.y -= self.ySpeed
        self.xSpeed = 0
        self.ySpeed -= self.gravity

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
            self.xSpeed -= 5

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and not self.block_r:
            self.xSpeed += 5

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.jumpsRemaining > 0:
                    self.jump()

        if self.block_u:
            self.ySpeed = 0
            self.player.rect.top += 5

        # Collision under
        if self.block_d:
            self.ySpeed = 0
            self.player.rect.bottom = (self.player.rect.bottom / 64 * 64)
            self.jumpsRemaining = 2


    def draw(self):
        surface = Artist.get_display()
      #  sprites = self.sprites()
        surface_blit = surface.blit
        surface_blit(self.player.image, self.player.rect)

       # self.player_group.draw(Artist.get_display())


    @staticmethod
    def set_spawn_x(spawn_x, spawn_y):
        PlayerNormalState.spawn_x = spawn_x
        PlayerNormalState.spawn_y = spawn_y

    #returns true when there is collision.
    def collision(self, group_1, group_2):
       pass

    def jump(self):
        self.ySpeed = 10
        self.jumpsRemaining -=1
