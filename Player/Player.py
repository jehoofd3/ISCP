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

    canGoRight = False
    canGoLeft = False
    collision_under = False
    collision_up = False

    half_screen_width = Artist.get_half_screen_width()
    face_direction = 'Right'

    jumpsRemaining = 0
    jumpWasPressed = None
    jumpPressed = None

    xSpeed = 0.0
    xSpeed_standing_still = 0
    ySpeed = 0
    start_x = 0
    start_y = 0
    is_shifting = False
    sliding = False

    health_image_full = pygame.image.load("../Data/Images/Health.png").convert_alpha()
    health_image_empty = pygame.image.load("../Data/Images/Health_empty.png").convert_alpha()

    lives = ['', '', '']

    level_state_manager = None

    player_under_image = None
    player_up_image = None
    player_left_image = None
    player_right_image = None

    jump_sound = None

    player_on_snow = False
    player_on_ice = False

    def __init__(self, x, y, level_state_manager):
        self.level_state_manager = level_state_manager
        for i in range(0, len(self.lives)):
            if i <= (self.level_state_manager.player_health - 1):
                self.lives[i] = self.health_image_full
            else:
                self.lives[i] = self.health_image_empty

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../Data/Images/Player/stand_r.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y
        self.jump_sound = pygame.mixer.music.load('../Data/Music/Levels/Jump.wav')

        self.walk_l = []
        self.walk_r = []

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
        self.player_under_image.image = pygame.image.load("../Data/OB.png").convert_alpha()
        self.player_under_image.rect = self.player_under_image.image.get_rect()

        # Player up sprite
        self.player_up_image = pygame.sprite.Sprite()
        self.player_up_image.image = pygame.image.load("../Data/OB.png").convert_alpha()
        self.player_up_image.rect = self.player_up_image.image.get_rect()

        # Player left sprite
        self.player_left_image = pygame.sprite.Sprite()
        self.player_left_image.image = pygame.image.load("../Data/LR.png").convert_alpha()
        self.player_left_image.rect = self.player_left_image.image.get_rect()

        # Player right sprite
        self.player_right_image = pygame.sprite.Sprite()
        self.player_right_image.image = pygame.image.load("../Data/LR.png").convert_alpha()
        self.player_right_image.rect = self.player_right_image.image.get_rect()

    def run(self):
        self.states.run()

    def update(self):
        self.states.update()

        # PLayer under
        self.player_under_image.rect.x = self.rect.x + 10
        self.player_under_image.rect.y = self.rect.y + 94

        # PLayer up
        self.player_up_image.rect.x = self.rect.x + 10
        self.player_up_image.rect.y = self.rect.y - 1

        # PLayer left
        self.player_left_image.rect.x = self.rect.x - 1
        self.player_left_image.rect.y = self.rect.y + 12

        # PLayer right
        self.player_right_image.rect.x = self.rect.x + 70
        self.player_right_image.rect.y = self.rect.y + 12

        if self.rect.bottom >= 960:
            self.kill()

    def draw(self):
        x = 0
        for i in range(0, len(self.lives)):
            Artist.get_display().blit(self.lives[i], (x, 50))
            x += 55

        Artist.draw_textures(self.animation.update(), self.rect)
        Artist.draw_textures(self.player_under_image.image, self.player_under_image.rect)
        Artist.draw_textures(self.player_up_image.image, self.player_up_image.rect)
        Artist.draw_textures(self.player_left_image.image, self.player_left_image.rect)
        Artist.draw_textures(self.player_right_image.image, self.player_right_image.rect)

    def jump(self):
        self.player_on_snow = False
        self.player_on_ice = False
        self.set_sliding(4)

        pygame.mixer.music.play()
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
            self.states = PlayerDieState(self)
            self.level_state_manager.player_health -= 1

    def get_player_x_speed(self):
        return self.xSpeed

    def get_player_x(self):
        return self.rect.x

    def set_sliding(self, speed):
            self.states.player_x_speed = speed

