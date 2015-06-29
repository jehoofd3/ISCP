import pygame
from Helpers.Artist import *
from PlayerNormalState import *
from PlayerDieState import *
from Animation.PlayerAnimation import *

class Player (pygame.sprite.Sprite):
    states, walk_l, walk_r = [], [], []
    dead_l, dead_r, jump_l, jump_r, stand_l, stand_r = None, None, None, None, None, None
    block_u, block_d, block_r, block_l = None, None, None, None
    dead = None

    canGoRight = True
    canGoLeft = True
    collision_under = False
    collision_up = False

    half_screen_width = Artist.get_half_screen_width()
    face_direction = 'Right'

    jumpsRemaining = 2
    jumpWasPressed = None
    jumpPressed = None
    health = 3
    xSpeed = 0
    ySpeed = 0
    start_x = 0
    start_y = 0
    is_shifting = False

    player_under_image = None
    player_up_image = None
    player_left_image = None
    player_right_image = None

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../Data/Images/Player/stand_r.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y

        for i in range(11):
            self.walk_l.append(pygame.image.load("../Data/Images/Player/Left/l_" + str(i) + ".png").convert_alpha())

        for i in range(11):
            self.walk_r.append(pygame.image.load("../Data/Images/Player/Right/r_" + str(i) + ".png").convert_alpha())

        self.jump_r = pygame.image.load("../Data/Images/Player/jump_r.png").convert_alpha()
        self.jump_l = pygame.image.load("../Data/Images/Player/jump_l.png").convert_alpha()
        self.dead_l = pygame.image.load("../Data/Images/Player/dead_l.png").convert_alpha()
        self.dead_r = pygame.image.load("../Data/Images/Player/dead_r.png").convert_alpha()
        self.stand_l = pygame.image.load("../Data/Images/Player/stand_l.png").convert_alpha()
        self.stand_r = pygame.image.load("../Data/Images/Player/stand_r.png").convert_alpha()

        self.animation = PlayerAnimation(self)

        self.states = PlayerNormalState(self)

        # Player under sprite
        self.player_under_image = pygame.sprite.Sprite()
        self.player_under_image.image = pygame.image.load("../Data/OB.png").convert()
        self.player_under_image.rect = self.player_under_image.image.get_rect()

        # Player up sprite
        self.player_up_image = pygame.sprite.Sprite()
        self.player_up_image.image = pygame.image.load("../Data/OB.png").convert()
        self.player_up_image.rect = self.player_up_image.image.get_rect()

        # Player left sprite
        self.player_left_image = pygame.sprite.Sprite()
        self.player_left_image.image = pygame.image.load("../Data/LR.png").convert()
        self.player_left_image.rect = self.player_left_image.image.get_rect()

        # Player right sprite
        self.player_right_image = pygame.sprite.Sprite()
        self.player_right_image.image = pygame.image.load("../Data/LR.png").convert()
        self.player_right_image.rect = self.player_right_image.image.get_rect()

    def run(self):
        self.states.run()

    def update(self):
        self.states.update()

        # PLayer under
        self.player_under_image.rect.x = self.rect.x + 5
        self.player_under_image.rect.y = self.rect.y + 94

        # PLayer up
        self.player_up_image.rect.x = self.rect.x + 5
        self.player_up_image.rect.y = self.rect.y - 10

        # PLayer left
        self.player_left_image.rect.x = self.rect.x - 10
        self.player_left_image.rect.y = self.rect.y + 12

        # PLayer right
        self.player_right_image.rect.x = self.rect.x + 70
        self.player_right_image.rect.y = self.rect.y + 12

    def draw(self):
        Artist.get_display().blit(self.animation.update(), self.rect)
        self.states.draw()
        Artist.get_display().blit(self.player_under_image.image, self.player_under_image.rect)
        Artist.get_display().blit(self.player_up_image.image, self.player_up_image.rect)
        Artist.get_display().blit(self.player_left_image.image, self.player_left_image.rect)
        Artist.get_display().blit(self.player_right_image.image, self.player_right_image.rect)

    def jump(self):
        self.ySpeed = 10
        self.jumpsRemaining -= 1

    def basic_movement(self):
        if not self.is_shifting:
            self.rect.x += self.xSpeed

        self.rect.y -= self.ySpeed
        self.xSpeed = 0

    def gravity(self):
        self.ySpeed -= 0.4

    def kill(self):
        if not self.dead:
            self.states.pop()
            self.states = [PlayerDieState(self)]
            self.health -= 1

    def get_player_x_speed(self):
        return self.xSpeed

    def get_player_x(self):
        return self.rect.x
