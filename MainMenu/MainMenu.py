import pygame
from Helpers.Artist import *
from LevelStateManager.Level1State import *
from LevelStateManager.Level2State import *
from LevelStateManager.Level3State import *
from LevelStateManager.Level4State import *
from OptionMenu import *
from Player.Player import *

class MainMenu(LevelState):

    mouse_pos = ''
    option_menu = None
    levelStateManager = None
    display = Artist.get_display()
    screen_width = Artist.get_screen_width()
    screen_height = Artist.get_screen_height()
    half_screen_width = Artist.get_half_screen_width()
    half_screen_height = Artist.get_half_screen_height()

    black_screen = pygame.image.load("../Data/Images/Menu/MainMenu/BlackScreen.png").convert()
    black_screen.set_alpha(0)
    lvl1 = pygame.image.load("../Data/Images/Menu/MainMenu/Lvl1.png").convert()

    background = pygame.image.load("../Data/Images/Menu/Background.png").convert()
    escape = pygame.image.load("../Data/Images/Menu/MainMenu/Escape.png").convert_alpha()
    ground = pygame.image.load("../Data/Images/Menu/Grass.png").convert_alpha()
    left_select_arrow = pygame.image.load("../Data/Images/Menu/MainMenu/SelectLeft.png").convert_alpha()
    right_select_arrow = pygame.image.load("../Data/Images/Menu/MainMenu/SelectRight.png").convert_alpha()

    main_menu_sprites = {'play': None, 'options': None, 'quit' : None}
    pressed_play = False
    alpha = 0
    fade_out_done = False
    music_faded = False

    def __init__(self, levelStateManager):
        self.options_menu = OptionMenu(self, levelStateManager)
        self.levelStateManager = levelStateManager
        self.make_sprite('play', "../Data/Images/Menu/MainMenu/Play.png", self.half_screen_width - 68, self.half_screen_height - 100)
        self.make_sprite('options', "../Data/Images/Menu/MainMenu/Options.png", self.half_screen_width - 68, self.half_screen_height - 20)
        self.make_sprite('quit', "../Data/Images/Menu/MainMenu/Quit.png", self.half_screen_width - 68, self.half_screen_height + 70)

    def run(self):
        pygame.mixer.music.load('../Data/Music/MainMenu/FeatherLight.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

    def draw(self):
        self.display.blit(self.background, (0, 0))

        #-215 is half image width
        self.display.blit(self.escape, (self.half_screen_width - 215, 100))

        self.display.blit(self.main_menu_sprites['play'].image, self.main_menu_sprites['play'].rect)
        self.display.blit(self.main_menu_sprites['options'].image, self.main_menu_sprites['options'].rect)
        self.display.blit(self.main_menu_sprites['quit'].image, self.main_menu_sprites['quit'].rect)

        #193 is ground image width
        self.display.blit(self.ground, (0, self.screen_height - 193))

        self.check_button_clicked()
        self.check_button_hovered()
        self.fade_out()

        self.display.blit(self.black_screen, (0, 0))

    def check_button_clicked(self):
        for event in pygame.event.get():
            # Loop stoppen wanneer het kruisje ingedrukt wordt
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.main_menu_sprites['play'].rect.collidepoint(self.mouse_pos):
                    self.pressed_play = True

                if self.main_menu_sprites['options'].rect.collidepoint(self.mouse_pos):
                    self.levelStateManager.states = self.options_menu

                if self.main_menu_sprites['quit'].rect.collidepoint(self.mouse_pos):
                    pygame.quit()
                    quit()

    def check_button_hovered(self):
        #hover play
        if self.main_menu_sprites['play'].rect.collidepoint(self.mouse_pos) and not self.pressed_play:
            self.display.blit(self.left_select_arrow, (self.main_menu_sprites['play'].rect.x - 90, self.main_menu_sprites['play'].rect.y))
            self.display.blit(self.right_select_arrow, (self.main_menu_sprites['play'].rect.x + 155, self.main_menu_sprites['play'].rect.y))

        #hover options
        if self.main_menu_sprites['options'].rect.collidepoint(self.mouse_pos) and not self.pressed_play:
            self.display.blit(self.left_select_arrow, (self.main_menu_sprites['options'].rect.x - 90, self.main_menu_sprites['options'].rect.y))
            self.display.blit(self.right_select_arrow, (self.main_menu_sprites['options'].rect.x + 155, self.main_menu_sprites['options'].rect.y))

        #hover quit
        if self.main_menu_sprites['quit'].rect.collidepoint(self.mouse_pos) and not self.pressed_play:
            self.display.blit(self.left_select_arrow, (self.main_menu_sprites['quit'].rect.x - 90, self.main_menu_sprites['quit'].rect.y))
            self.display.blit(self.right_select_arrow, (self.main_menu_sprites['quit'].rect.x + 155, self.main_menu_sprites['quit'].rect.y))

    def fade_out(self):
        if self.pressed_play and self.alpha <= 255 and not self.fade_out_done:
            self.alpha += 3
            self.black_screen.set_alpha(self.alpha)

            if self.alpha >= 255:
                self.fade_out_done = True

        elif self.pressed_play:
            self.alpha -= 2
            self.black_screen.set_alpha(self.alpha)
            self.display.blit(self.lvl1, (0, 0))

            if self.alpha <= 0:
                self.pressed_play = False
                self.fade_out_done = False
                self.levelStateManager.states = Level4State(self.levelStateManager, self)

        if self.pressed_play and not self.music_faded:
            pygame.mixer.music.fadeout(1000)

    def make_sprite(self, button_name, image_location, width, height):
        self.main_menu_sprites[button_name] = pygame.sprite.Sprite()
        self.main_menu_sprites[button_name].image = pygame.image.load(image_location).convert_alpha()
        self.main_menu_sprites[button_name].rect = self.main_menu_sprites[button_name].image.get_rect()
        self.main_menu_sprites[button_name].rect.x = width
        self.main_menu_sprites[button_name].rect.y = height
