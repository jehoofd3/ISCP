import pygame
from Helpers.Artist import *
from Map.TileGrid import *

class PlayerNormalState:

    walk_l = []
    walk_r = []

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
        self.jumpWasPressed = False
        self.jumpPressed = False

    def run(self):
        pass

    def update(self):
        self.player.rect.x += self.xSpeed
        self.player.rect.y -= self.ySpeed

        self.xSpeed = 0

        self.ySpeed -= self.gravity

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.xSpeed -= 5

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.xSpeed += 5

        blocks_hit_list = pygame.sprite.spritecollide(self.player, TileGrid.get_group(), False)

        for block in blocks_hit_list:
            self.player.rect.bottom = block.rect.top

            if self.player.rect.bottom >= block.rect.top:
                self.player.rect.bottom = block.rect.top

            if self.xSpeed > 0 and self.player.rect.bottom == block.rect.bottom:
                    self.player.rect.right = block.rect.left

            print block.rect.top
            print block.rect.bottom
            print block.rect.left
            print block.rect.right


        if len(blocks_hit_list) != 0:
            self.ySpeed = 0
            self.gravity = 0
        else:
            self.gravity = 0.4

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

    '''

         def draw(self, surface):
        """draw all sprites onto the surface

        Group.draw(surface): return None

        Draws all of the member sprites onto the given surface.

        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []



       # blocks_hit_list = pygame.sprite.spritecollideany(self.player_group, TileGrid.get_group())
        #blocks_hit_list = pygame.sprite.spritecollide(self.player_group, TileGrid.get_group(), True)
        #blocks_hit_list = pygame.sprite.groupcollide(TileGrid.get_group(), TileGrid.get_group(), False, False)
           for block in blocks_hit_list:
            self.rect.bottom = block.rect.top
            print block.rect.top
            print block.rect.bottom
            print block.rect.left
            print block.rect.right
            print 'block'

        if len(blocks_hit_list) != 0:
            self.ySpeed = 0
            self.gravity = 0
'''
