import pygame
from Helpers.Artist import *
from Helpers.DatabaseReceiver import *
from LevelStateManager.LevelState import *

# Author: Richard Jongenburger


class OptionMenu(LevelState):
    # We need a mouse position variable to know whether we
    # clicked on a sprite.
    mouse_pos = ''

    # Save the main menu reference.
    # So we don't create a new MainMenu object everytime we open the
    # main menu.
    main_menu = None

    # Create a reference to the LevelStateManager
    # so we can open the main menu when you click on the back sprite.
    level_state_manager = None

    # Get the width and height of the game window.
    # This is needed for the x and y values of the sprites.
    screen_width = Artist.get_screen_width()
    screen_height = Artist.get_screen_height()

    # Gets half of the width and height of the game window.
    # It's handy to get the half of the game window width and height,
    # so you can put the objects in the middle.
    half_screen_width = Artist.get_half_screen_width()
    half_screen_height = Artist.get_half_screen_height()

    # Get all the images from the database.
    background = DatabaseReceiver\
        .get_menu_img("Background")
    options = DatabaseReceiver\
        .get_menu_img("Options_Options")
    music = DatabaseReceiver\
        .get_menu_img("Options_Music")
    music_bullet_empty_image = DatabaseReceiver\
        .get_menu_img("Options_BulletEmpty")
    music_bullet_full_image = DatabaseReceiver\
        .get_menu_img("Options_BulletFull")
    check_box_empty_image = DatabaseReceiver\
        .get_menu_img("Options_ClickButtonEmpty")
    check_box_full_image = DatabaseReceiver\
        .get_menu_img("Options_ClickButtonFull")
    fullscreen = DatabaseReceiver\
        .get_menu_img("Options_Fullscreen")
    ground = DatabaseReceiver\
        .get_menu_img("Grass")

    # This is a simulation of the bullet points in the option menu.
    # There are 6 bullets.
    # 1 = on , 0 = off.
    music_bullets = [1, 1, 1, 0, 0, 0]

    # This is the position of the
    # last bullet that is full (on) in the music_bullets array.
    position_last_full_bullet = 2

    # X and Y position of the first bullet.
    bullet_x = None
    bullet_y = half_screen_height - 97

    # Variable to know if fullscreen is turned on.
    fullscreen_on = False

    # Makes an array for all the option menu sprites.
    options_sprites = {'check_box': None, 'quit': None}

    # Half of the images width.
    # So we place the images in the middle of the surface.
    half_images_width = 215

    # Half of the ground image height
    # to put the y value of the ground in the middle.
    half_ground_image_height = 193

    # Current volume level. The volume ranges from 0 up to 1.
    # 0 is no sound and 1 is the loudest you can get.
    music_volume_level = 0.4

    def __init__(self, main_menu, level_state_manager):
        self.mainMenu = main_menu
        self.level_state_manager = level_state_manager

        # Makes sprites for all the buttons with there respective name,
        # image, x and y.
        self.make_sprite('select_left',
                         DatabaseReceiver.get_menu_img("SelectLeft"),
                         self.half_screen_width + 5,
                         self.half_screen_height - 115)
        self.make_sprite('select_right',
                         DatabaseReceiver.get_menu_img("SelectRight"),
                         self.half_screen_width + 230,
                         self.half_screen_height - 115)
        self.make_sprite('check_box',
                         DatabaseReceiver.
                         get_menu_img("Options_ClickButtonEmpty"),
                         self.half_screen_width + 10,
                         self.half_screen_height - 50)
        self.make_sprite('back',
                         DatabaseReceiver.get_menu_img("Options_Back"),
                         self.half_screen_width - 68,
                         self.half_screen_height + 70)

    def run(self):
        pass

    def update(self):
        # Sets the mouse position every frame.
        self.mouse_pos = pygame.mouse.get_pos()

    def draw(self):
        # Draws the background.
        Artist.draw_textures(self.background, (0, 0))

        # Draws all the sprites.
        Artist.draw_textures(self.options, (self.half_screen_width -
                                            self.half_images_width, 100))
        Artist.draw_textures(self.music, (self.half_screen_width -
                                          self.half_images_width,
                                          self.half_screen_height - 110))
        Artist.draw_textures(self.fullscreen, (self.half_screen_width -
                                               self.half_images_width,
                                               self.half_screen_height - 50))
        Artist.draw_textures(self.options_sprites['select_left'].image,
                             self.options_sprites['select_left'].rect)
        Artist.draw_textures(self.options_sprites['select_right'].image,
                             self.options_sprites['select_right'].rect)
        Artist.draw_textures(self.options_sprites['check_box'].image,
                             self.options_sprites['check_box'].rect)
        Artist.draw_textures(self.options_sprites['back'].image,
                             self.options_sprites['back'].rect)

        self.bullet_x = self.half_screen_width + 70

        # Loop through all the bullets in the music bullets array.
        for bullet in self.music_bullets:
            # When the bullet is 1, draw the bullet_full_image.
            if bullet == 1:
                Artist.draw_textures(self.music_bullet_full_image,
                                     (self.bullet_x, self.bullet_y))
            # When the bullet is 0, draw the bullet_empty_image.
            else:
                Artist.draw_textures(self.music_bullet_empty_image,
                                     (self.bullet_x, self.bullet_y))

            # Sets the space between the bullets.
            self.bullet_x += 30

        # Draw the ground.
        Artist.draw_textures(self.ground, (0, self.screen_height -
                                           self.half_ground_image_height))

        self.check_button_clicked()

    def check_button_clicked(self):
        # Event handling:
        # With pygame.event.get(),
        # you get all of the mouse/keyboard
        # input events in pygame's event queue.
        # The pygame.MOUSEBUTTONDOWN event is created
        # when you click on the left mouse button.
        # Those events are automatically removed from the queue,
        # when you call pygame.event.get() method.
        # So basically it loops trough all the events
        # that are returned from pygame.event.get()
        for event in pygame.event.get():
            # To test whether the event is a mouse button event.
            # So if it is a MOUSEBUTTONDOWN event,
            # it know you clicked with the left mouse button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # To test if the mouse position collide
                # with the select_left sprite.
                # And to check if the last full button isn't zero.
                # if the last full bullet is zero,
                # you can't go to the left because
                # there aren't more bullets left.
                if self.position_last_full_bullet != 0 and \
                        self.options_sprites['select_left'].rect.collidepoint(
                            self.mouse_pos):
                    # Sets the music level with 0.2
                    # lower than the current level.
                    self.music_volume_level -= 0.2
                    pygame.mixer.music.set_volume(self.music_volume_level)

                    # Sets the last full bullet one to the left.
                    self.music_bullets[self.position_last_full_bullet] = 0
                    self.position_last_full_bullet -= 1

                # To test if the mouse position
                # collide with the select_right sprite.
                # And to check if the last full button isn't five.
                # if the last full bullet is five,
                # you can't go to the right,
                # because there aren't more bullets left.
                if self.position_last_full_bullet != 5 and \
                        self.options_sprites['select_right'].rect.collidepoint(
                            self.mouse_pos):
                    self.music_volume_level += 0.2
                    pygame.mixer.music.set_volume(self.music_volume_level)

                    # Sets the last full bullet one to the right.
                    self.music_bullets[self.position_last_full_bullet + 1] = 1
                    self.position_last_full_bullet += 1

                # To test if the mouse position collide
                # with the check_box sprite.
                if self.options_sprites['check_box'].rect.collidepoint(
                        self.mouse_pos):
                    # If the window isn't fullscreen, make it
                    # fullscreen.
                    if not self.fullscreen_on:
                        self.fullscreen_on = True
                        # Sets the check box checked.
                        self.options_sprites['check_box'].image = \
                            self.check_box_full_image
                        # Pygame method to set the window fullscreen
                        # with the specified with and height. (960x768)
                        pygame.display.set_mode((self.screen_width,
                                                 self.screen_height),
                                                pygame.FULLSCREEN)
                    # If the window is fullscreen, make it windowed.
                    elif self.fullscreen_on:
                        self.fullscreen_on = False
                        # Sets the check box unchecked.
                        self.options_sprites['check_box'].image = \
                            self.check_box_empty_image
                        # Pyagme method to set the window as windowed
                        # with the specified with and height.(960x768)
                        pygame.display.set_mode((self.screen_width,
                                                 self.screen_height))

                # Check if the back button collides with the mouse
                # position.
                # Switch the current state in levelStateManger
                # back to the mainMenu state.
                if self.options_sprites['back'].rect.collidepoint(
                        self.mouse_pos):
                    self.LevelStateManager.states = self.mainMenu

    # Method that makes a pygame sprite and put that sprite in an array.
    def make_sprite(self, button_name, image, x, y):
        # pygame.sprite.Sprite is used to create a sprite object.
        self.options_sprites[button_name] = pygame.sprite.Sprite()

        # Sets the image of the sprite.
        self.options_sprites[button_name].image = image

        # Get the rectangle values of an image.
        self.options_sprites[button_name].rect = \
            self.options_sprites[button_name].image.get_rect()

        # Sets the position of the image.
        self.options_sprites[button_name].rect.x = x
        self.options_sprites[button_name].rect.y = y
