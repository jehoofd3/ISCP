import pygame
from Helpers.Artist import *
from Helpers.DatabaseReceiver import *
from LevelStateManager.Level1State import *
from LevelStateManager.Level2State import *
from LevelStateManager.Level3State import *
from LevelStateManager.Level4State import *
from OptionMenu import *
from Player.Player import *

# Author: Richard Jongenburger.


class MainMenu(LevelState):
    # We need a mouse position variable to know whether we clicked on a sprite.
    mouse_pos = ''

    # Save the option menu reference.
    # So we don't create a new OptionMenu object
    # everytime we open the option menu.
    option_menu = None

    # Create a reference to the LevelStateManager
    # so we can open the first level when you click on play.
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
    resume = DatabaseReceiver.get_menu_img("Options_Resume")
    background = DatabaseReceiver.get_menu_img("Background")
    escape = DatabaseReceiver.get_menu_img("Escape")
    ground = DatabaseReceiver.get_menu_img("Grass")
    left_select_arrow = DatabaseReceiver.get_menu_img("SelectLeft")
    right_select_arrow = DatabaseReceiver.get_menu_img("SelectRight")
    black_screen = DatabaseReceiver.get_menu_img("BlackScreen").convert()
    lvl1 = DatabaseReceiver.get_menu_img("lvl1")

    # Sets the alpha of the image at zero. So that the image is transparent.
    black_screen.set_alpha(0)

    # Makes an array for all the main menu sprites.
    main_menu_sprites = {'play': None, 'options': None, 'quit': None}

    # Variables to determine whether we pressed on the play button.
    first_time_pressed_play = True
    pressed_play = False

    # Used to keep track of the alpha on the black_screen_image.
    alpha = 0

    # Used to test if the fade out is done.
    fade_out_done = False

    # Boolean that represent if the music is faded.
    music_faded = False

    # Needed so we can place the images
    # exactly in the middle when drawing on the screen.
    half_escape_image_width = 215
    half_ground_image_width = 193

    def __init__(self, level_state_manager):
        self.options_menu = OptionMenu(self, level_state_manager)

        self.level_state_manager = level_state_manager

        # Make the play, option,
        # quit sprites with the images and the x and y values.
        self.make_sprite('play', DatabaseReceiver.get_menu_img("Play"),
                         self.half_screen_width - 68,
                         self.half_screen_height - 100)
        self.make_sprite('options', DatabaseReceiver.get_menu_img("Options"),
                         self.half_screen_width - 68,
                         self.half_screen_height - 20)
        self.make_sprite('quit', DatabaseReceiver.get_menu_img("Quit"),
                         self.half_screen_width - 68,
                         self.half_screen_height + 70)

    def run(self):
        # Load music.
        pygame.mixer.music.load('../Data/Music/MainMenu/FeatherLight.mp3')
        # Set the start volume at 0.4.
        pygame.mixer.music.set_volume(0.4)
        # Play the music in a loop.
        pygame.mixer.music.play()

    def update(self):
        # Sets the mouse position every frame.
        self.mouse_pos = pygame.mouse.get_pos()

    def draw(self):
        # Draw the background on the surface.
        Artist.draw_textures(self.background, (0, 0))

        # Draw the sprites on the surface.
        Artist.draw_textures(self.escape, (self.half_screen_width -
                                           self.half_escape_image_width, 100))
        Artist.draw_textures(self.main_menu_sprites['play'].image,
                             self.main_menu_sprites['play'].rect)
        Artist.draw_textures(self.main_menu_sprites['options'].image,
                             self.main_menu_sprites['options'].rect)
        Artist.draw_textures(self.main_menu_sprites['quit'].image,
                             self.main_menu_sprites['quit'].rect)
        Artist.draw_textures(self.ground, (0, self.screen_height -
                                           self.half_ground_image_width))

        # Method to check if a sprite is clicked.
        self.check_button_clicked()

        # Method to check if the user is hovering over the sprites.
        self.check_button_hovered()

        # Used to fade-out and fade-in when you click on the player sprite.
        self.fade_out()

        # Draw the black screen. This is needed for the fade-out.
        Artist.draw_textures(self.black_screen, (0, 0))

    def check_button_clicked(self):
        # Event handling:
        # With pygame.event.get(), you get all of the mouse/keyboard
        # input events in pygame's event queue.
        # Those events are automatically removed from the queue,
        # when you call pygame.event.get() method.
        # So basically it loops trough all the events
        # that are returned from pygame.event.get().
        for event in pygame.event.get():
            # To test whether the event is a mouse button event.
            # So if it is a MOUSEBUTTONDOWN event,
            # it knows you clicked with the left mouse button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # To test if the mouse position collide with the play sprite.
                # So it knows if the play button is clicked
                #  and not some other object.
                if self.main_menu_sprites['play'].rect.collidepoint(
                        self.mouse_pos):
                    # Check if it is the first time you pressed play.
                    # If it is, set the variables accordingly.
                    # These statements are necessary to open a
                    # different MainMenu when you click the play sprite for
                    # a second time.
                    # This second MainMenu contains a resume button
                    # and you resume the game instead of starting the game.
                    if self.first_time_pressed_play:
                        self.pressed_play = True
                        self.first_time_pressed_play = False
                    # If you pressed the play sprite for the second time,
                    # resume the game instead of starting the game.
                    else:
                        self.level_state_manager.states = \
                            self.level_state_manager.level_state
                        self.level_state_manager.level_state = None
                        self.level_state_manager.set_jump_sound(
                            self.options_menu.music_volume_level)

                # If the mouse position collides with the option sprite,
                # open the option menu.
                if self.main_menu_sprites['options'].rect.collidepoint(
                        self.mouse_pos):
                    self.level_state_manager.states = self.options_menu

                # Quit the program when you pressed the quit sprite.
                if self.main_menu_sprites['quit'].rect.collidepoint(
                        self.mouse_pos):
                    pygame.quit()
                    quit()

    def check_button_hovered(self):
        # First we test if the mouse position
        # is colliding with the given sprite,
        # so we know tat the user is hovering over the image.
        # Then we test if the play button isn't pressed.
        # So that the hovers don't work if the player pressed play.
        # If we hover on any of the player, option or quit sprite,
        # we draw select arrows around them.
        # The images are drawn with the draw_textures method in the artist
        # class. It needs the image, x and y.

        # hover play
        if self.main_menu_sprites['play'].rect.collidepoint(
                self.mouse_pos) and not self.pressed_play:
            # Draw the select arrows with their image, x and y.
            Artist.draw_textures(self.left_select_arrow, (
                self.main_menu_sprites['play'].rect.x - 90,
                self.main_menu_sprites['play'].rect.y))
            Artist.draw_textures(self.right_select_arrow,
                                 (self.main_menu_sprites['play'].rect.x + 155,
                                  self.main_menu_sprites['play'].rect.y))

        # hover options
        if self.main_menu_sprites['options'].rect.collidepoint(
                self.mouse_pos) and not self.pressed_play:
            # Draw the select arrows with their image, x and y.
            Artist.draw_textures(self.left_select_arrow, (
                self.main_menu_sprites['options'].rect.x - 90,
                self.main_menu_sprites['options'].rect.y))
            Artist.draw_textures(self.right_select_arrow, (
                self.main_menu_sprites['options'].rect.x + 155,
                self.main_menu_sprites['options'].rect.y))

        # hover quit
        if self.main_menu_sprites['quit'].rect.collidepoint(self.mouse_pos) \
                and not self.pressed_play:
            # Draw the select arrows with their image, x and y.
            Artist.draw_textures(self.left_select_arrow, (
                self.main_menu_sprites['quit'].rect.x - 90,
                self.main_menu_sprites['quit'].rect.y))
            Artist.draw_textures(self.right_select_arrow, (
                self.main_menu_sprites['quit'].rect.x + 155,
                self.main_menu_sprites['quit'].rect.y))

    # Method to fade-out from the main menu and fade-in in level 1.
    def fade_out(self):
        # We got a black image with an alpha value.
        # That value can range from 0 up to 255.
        # The image is transparent when the alpha value is 0,
        # and fully visible when the alpha value is 255.
        # When the player pressed play and the alpha value is smaller then 255.
        # We up the alpha with 3.
        if self.pressed_play and self.alpha <= 255 and not self.fade_out_done:
            self.alpha += 3
            self.black_screen.set_alpha(self.alpha)

            # When the alpha is above 255, then the fade out is done.
            if self.alpha >= 255:
                self.fade_out_done = True

        # When the player pressed play and the fade out is done,
        # up the alpha with -3 and draw an image of the spawn point of level 1.
        elif self.pressed_play and self.fade_out_done:
            self.alpha -= 3
            self.black_screen.set_alpha(self.alpha)
            Artist.draw_textures(self.lvl1, (0, 0))
        # If the alpha is zero or less, open level 1.
            if self.alpha <= 0:
                # Set the boolea values back to their starting value.
                self.pressed_play = False
                self.fade_out_done = False
                # Set the level in the LevelStateManager class to 1.
                self.level_state_manager.states.level = 1
                # Set the image of the play button as resume.
                # Because we make it a resume menu after you pressed
                # play on the first menu.
                self.main_menu_sprites['play'].image = self.resume
                self.level_state_manager.open_level1()
                # Set the volume level of the jump sound
                # as what the player set it to in the option menu.
                self.level_state_manager.set_jump_sound(
                    self.options_menu.music_volume_level)

        # Fade out the music when you pressed play and the music isn't faded.
        if self.pressed_play and not self.music_faded:
            pygame.mixer.music.fadeout(1000)

    # Method that makes a pygame sprite and put that sprite in an array.
    def make_sprite(self, button_name, image, x, y):
        # pygame.sprite.Sprite is used to create a sprite object.
        self.main_menu_sprites[button_name] = pygame.sprite.Sprite()

        # Sets the image of the sprite.
        self.main_menu_sprites[button_name].image = image

        # Get the rectangle values of an image.
        # The rectangle exists of 4 ints.
        # The x, y, width and height.
        self.main_menu_sprites[button_name].rect = \
            self.main_menu_sprites[button_name].image.get_rect()

        # Sets the x and y position of the image.
        self.main_menu_sprites[button_name].rect.x = x
        self.main_menu_sprites[button_name].rect.y = y
