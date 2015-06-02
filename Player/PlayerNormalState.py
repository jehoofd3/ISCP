import pygame
from Helpers.Artist import *

class PlayerNormalState(pygame.sprite.Sprite):

    walk_l = []
    walk_r = []

    spawn_x = 10
    spawn_y = 10
    image_player = "../Data/Images/p2_front.png"

    def __init__(self):
        self.player_group = pygame.sprite.Group()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.image_player).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
        self.player_group.add(self)

        self.xSpeed = 0
        self.ySpeed = 0
        self.jumpsRemaining = 2
        self.jumpWasPressed = False
        self.jumpPressed = False

    def run(self):
        pass

    def update(self):

        self.rect.x += self.xSpeed
        self.rect.y -= self.ySpeed

        self.xSpeed = 0

        self.ySpeed -= 0.4
        print self.rect.y

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.xSpeed -= 5

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.xSpeed += 5

        for event in pygame.event.get():
            if event.type == pygame.K_UP:
                self.jump()

    def draw(self):
        self.player_group.draw(Artist.get_display())

    '''      # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self.player, self.map.get_group(), False)
        for block in block_hit_list:
            print block_hit_list

            if self.player.xSpeed > 0:
                self.player.rect.right = block.rect.left
                print "a"
            elif self.player.xSpeed < 0:
                self.player.rect.left = block.rect.right
                print "b"


            self.player.rect.bottom = block.rect.top

            if self.player.ySpeed > 0:
                self.player.rect.top = block.rect.bottom
            elif self.player.ySpeed < 0:
                self.player.rect.bottom = block.rect.top

    '''