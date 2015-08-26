import pygame
from Helpers.Artist import *
from Helpers.DatabaseReceiver import *
from LevelStateManager.LevelState import *

class OptionMenu(LevelState):

    screen_width = Artist.get_screen_width()
    screen_height = Artist.get_screen_height()
    half_screen_width = Artist.get_half_screen_width()
    half_screen_height = Artist.get_half_screen_height()

    background = DatabaseReceiver.get_menu_img("Background")
    options = DatabaseReceiver.get_menu_img("Options_Options")

    # music
    music = DatabaseReceiver.get_menu_img("Options_Music")
    music_bullet_empty_image = DatabaseReceiver.get_menu_img("Options_BulletEmpty")
    music_bullet_full_image = DatabaseReceiver.get_menu_img("Options_BulletFull")
    music_bullets = [1, 1, 1, 0, 0, 0]
    current_last_full = 2
    bullet_with = None
    bullet_height = half_screen_height - 97

    fullscreen = DatabaseReceiver.get_menu_img("Options_Fullscreen")
    ground = DatabaseReceiver.get_menu_img("Grass")

    mainMenu = None
    levelStateManager = None
    fullscreen_on = False

    click_button_empty_image = DatabaseReceiver.get_menu_img("Options_ClickButtonEmpty")
    click_button_full_image = DatabaseReceiver.get_menu_img("Options_ClickButtonFull")

    options_sprites = {'click_button': None, 'quit': None}
    musc_volume_level = 0.4
    mainMenu = None
    levelStateManager = None
    fullscreen_on = False

    levelStateManager = None

    def __init__(self, mainMenu, levelStateManager):
        self.mainMenu = mainMenu
        self.levelStateManager = levelStateManager

        self.make_sprite('select_left', DatabaseReceiver.get_menu_img("SelectLeft"), self.half_screen_width + 5, self.half_screen_height - 115)
        self.make_sprite('select_right', DatabaseReceiver.get_menu_img("SelectRight"), self.half_screen_width + 230, self.half_screen_height - 115)

        self.make_sprite('click_button', DatabaseReceiver.get_menu_img("Options_ClickButtonEmpty"), self.half_screen_width + 10, self.half_screen_height - 50)
        self.make_sprite('back', DatabaseReceiver.get_menu_img("Options_Back"), self.half_screen_width - 68, self.half_screen_height + 70)

    def run(self):
        pass

    def update(self):
        mous_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Loop stoppen wanneer het kruisje ingedrukt wordt
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_last_full != 0 and self.options_sprites['select_left'].rect.collidepoint(mous_pos):
                    self.musc_volume_level -= 0.2
                    pygame.mixer.music.set_volume(self.musc_volume_level)
                    self.music_bullets[self.current_last_full] = 0
                    self.current_last_full -= 1

                if self.current_last_full != 5 and self.options_sprites['select_right'].rect.collidepoint(mous_pos):
                    self.musc_volume_level += 0.2
                    pygame.mixer.music.set_volume(self.musc_volume_level)
                    self.music_bullets[self.current_last_full + 1] = 1
                    self.current_last_full += 1

                if self.options_sprites['click_button'].rect.collidepoint(mous_pos):
                    if not self.fullscreen_on:
                        self.fullscreen_on = True
                        self.options_sprites['click_button'].image = self.click_button_full_image
                        pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
                    elif self.fullscreen_on:
                        self.fullscreen_on = False
                        self.options_sprites['click_button'].image = self.click_button_empty_image
                        pygame.display.set_mode((self.screen_width, self.screen_height))

                if self.options_sprites['back'].rect.collidepoint(mous_pos):
                    self.levelStateManager.states = self.mainMenu

    def draw(self):
        Artist.draw_textures(self.background, (0, 0))

        #-215 is half image width
        Artist.draw_textures(self.options, (self.half_screen_width - 215, 100))
        Artist.draw_textures(self.music, (self.half_screen_width - 215, self.half_screen_height - 110))
        Artist.draw_textures(self.fullscreen, (self.half_screen_width - 215, self.half_screen_height - 50))

        Artist.draw_textures(self.options_sprites['select_left'].image, self.options_sprites['select_left'].rect)
        Artist.draw_textures(self.options_sprites['select_right'].image, self.options_sprites['select_right'].rect)

        Artist.draw_textures(self.options_sprites['click_button'].image, self.options_sprites['click_button'].rect)
        Artist.draw_textures(self.options_sprites['back'].image, self.options_sprites['back'].rect)

        self.bullet_with = self.half_screen_width + 70

        for bullet in self.music_bullets:
            if bullet == 1:
                Artist.draw_textures(self.music_bullet_full_image, (self.bullet_with, self.bullet_height))
            else:
                Artist.draw_textures(self.music_bullet_empty_image, (self.bullet_with, self.bullet_height))

            #de ruimte tussen de bullets
            self.bullet_with += 30


        #193 is ground image width
        Artist.draw_textures(self.ground, (0, self.screen_height - 193))

    def make_sprite(self, button_name, image, width, height):
        self.options_sprites[button_name] = pygame.sprite.Sprite()
        self.options_sprites[button_name].image = image
        self.options_sprites[button_name].rect = self.options_sprites[button_name].image.get_rect()
        self.options_sprites[button_name].rect.x = width
        self.options_sprites[button_name].rect.y = height
