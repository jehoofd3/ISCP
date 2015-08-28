import pygame
from Helpers.Artist import *
from Helpers.DatabaseReceiver import *
from PlayerNormalState import *
from PlayerDieState import *
from Animation.PlayerAnimation import *
from Helpers.DatabaseReceiver import *


class Player(pygame.sprite.Sprite):
    # The states variable is a object to store the states of the player.
    # The walk_l and walk_r lists are used to store images.
    states, walk_l, walk_r = [], [], []

    # The dead_l and dead_r variables are the images used if the,
    # player is dead.
    # The jump_l and jump_r variables are the images used if the,
    # player jumps.
    # The stand_l and stand_r variables are the images used if the,
    # player stands still.
    dead_l, dead_r, jump_l = None, None, None
    jump_r, stand_l, stand_r = None, None, None

    # The four booleans block_u, block_d, block_r and block_l indicates
    # if the player is colliding with other objects.
    # These variables are set true or false by the collider.
    # The player uses it to see if it can move a particular position.
    block_u, block_d, block_r, block_l = None, None, None, None

    # The dead boolean is False if the player is alive and True if it is
    # dead an can be set by the collider or the player himself.
    dead = None

    # These two booleans represent if the player can move to the left
    # and to ther right. It's used by the collider.
    can_go_right = False
    can_go_left = False

    # These booleans are to determine if there is collision above the
    # player and under the player.
    collision_under = False
    collision_up = False

    # Variable used to place object in the middle of the screen.
    half_screen_width = Artist.get_half_screen_width()

    # Variable with a string that can has 2 values: 'Left' or 'Right'.
    # It is the direction the player is facing.
    # It's used in the collider for the sliding on snow or ice.
    face_direction = 'Right'

    # The jumps_remaining variable is an integer and controls the
    # player's jumps.
    # He can only jump one time.
    jumps_remaining = 0

    # This variable is an integer and used to let the player move on the
    # x axis.
    x_speed = 0

    # This variable is used to let the player move on the y axis.
    y_speed = 0

    # Here comes the player's spawn point when we create the player.
    start_x = 0
    start_y = 0

    # Variable that represent if the map is shifting or not.
    # It's used to make the camera work.
    is_shifting = False

    # Get the health images from the database.
    health_image_full = DatabaseReceiver.get_player_img("Health_Full")
    health_image_empty = DatabaseReceiver.get_player_img("Health_Empty")

    # This array represents the lives the player has.
    lives = ['', '', '']

    level_state_manager = None

    # These variables are used to calculate the collision.
    # It is hard to explain in comments.
    # We explain it in the report.
    player_under_image = None
    player_up_image = None
    player_left_image = None
    player_right_image = None

    # Variable to hold the jump sound file.
    jump_sound = None

    # Variable that represents if the player collides with a snow
    # or ice tile.
    # It's set in the Collider class.
    player_on_snow = False
    player_on_ice = False

    def __init__(self, x, y, level_state_manager):
        self.level_state_manager = level_state_manager

        # Loop through the lives array.
        for i in range(0, len(self.lives)):
            # These statements are used to fill the lives array with
            # full or empty live images. It's filled by using the
            # player_health variable in LevelStateManager class.
            # First we do the player's health int variable minus one.
            # We do this because the player's health variable in the
            # LevelStateManager class start from 1.
            # And the array here start from 0.
            # So the array will be filled with health_image_full images
            # until the value of player_health - 1 is reached.
            if i <= (self.level_state_manager.player_health - 1):
                self.lives[i] = self.health_image_full
            else:
                self.lives[i] = self.health_image_empty

        # Initialize the sprite class. (pygame library)
        pygame.sprite.Sprite.__init__(self)

        # self.rect is a list of four ints x, y, width and height.
        # The draw method in Artist needs this data to draw
        # the image properly.
        # The get_rect() method on the image only places the width and
        # height in the rect variable.
        self.rect = DatabaseReceiver.get_player_img("stand_r").get_rect()

        # The rect.x variable is a method to change the x variable in rect.
        # Because the image doesn't have a x and y in the beginning,
        # it has to be changed in this way.
        self.rect.x = x

        # The rect.y variable is a method to change the y variable
        # in rect.
        # Because the image doesn't have a x and y in the beginning,
        # it has to be changed in this way.
        self.rect.y = y

        # The start_x and start_y are integers used to set the player
        # back to his original position after he died.
        self.start_x = x
        self.start_y = y

        # Call the sound method from the pygame.mixer class.
        # It needs the file of the mp3 or wav.
        # We put it in the jump_sound variable.
        self.jump_sound = pygame.mixer.Sound('../Data/Music/Levels/Jump.wav')

        # The speed integer is used to calculate the speed of the player
        # on the x axis.
        self.speed = 4

        # These line of code clears the walk_l and walk_r lists.
        self.walk_l = []
        self.walk_r = []

        # This for loop loops 10 times.
        for i in range(11):
            # It adds an image from the database to the walk_l list.
            # There are 10 images, 0 - 9.
            # The i in the loop is used to get the right image.
            self.walk_l.append(DatabaseReceiver.get_player_img("l_" +
                                                               str(i) + ""))

            # It adds an image from the database to the walk_r list.
            # There are 10 images, 0 - 9.
            # The i in the loop is used to get the right image.
            self.walk_r.append(DatabaseReceiver.get_player_img("r_" +
                                                               str(i) + ""))

        # These line of codes adds images from the database to the variables.
        self.jump_r = DatabaseReceiver.get_player_img("jump_r")
        self.jump_l = DatabaseReceiver.get_player_img("jump_l")
        self.dead_l = DatabaseReceiver.get_player_img("dead_l")
        self.dead_r = DatabaseReceiver.get_player_img("dead_r")
        self.stand_l = DatabaseReceiver.get_player_img("stand_l")
        self.stand_r = DatabaseReceiver.get_player_img("stand_r")

        # This line of code creates an PlayerAnimation object.
        # It is used to calculate the animation.
        self.animation = PlayerAnimation(self)

        # When the player is created this line of code changes the
        # states object into PlayerNormalState.
        self.states = PlayerNormalState(self)

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_under_image = pygame.sprite.Sprite()
        self.player_under_image.image = DatabaseReceiver.get_player_img("OB")
        self.player_under_image.rect = self.player_under_image.image.get_rect()

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_up_image = pygame.sprite.Sprite()
        self.player_up_image.image = DatabaseReceiver.get_player_img("OB")
        self.player_up_image.rect = self.player_up_image.image.get_rect()

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_left_image = pygame.sprite.Sprite()
        self.player_left_image.image = DatabaseReceiver.get_player_img("LR")
        self.player_left_image.rect = self.player_left_image.image.get_rect()

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_right_image = pygame.sprite.Sprite()
        self.player_right_image.image = DatabaseReceiver.get_player_img("LR")
        self.player_right_image.rect = self.player_right_image.image.get_rect()

    def run(self):
        # This line of code calls the run method in the state.
        self.states.run()

    def update(self):
        # This line of code calls the update method in the state.
        self.states.update()

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_under_image.rect.x = self.rect.x + 10
        self.player_under_image.rect.y = self.rect.y + 94

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_up_image.rect.x = self.rect.x + 10
        self.player_up_image.rect.y = self.rect.y - 1

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_left_image.rect.x = self.rect.x - 1
        self.player_left_image.rect.y = self.rect.y + 12

        # This variable is an image and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.player_right_image.rect.x = self.rect.x + 70
        self.player_right_image.rect.y = self.rect.y + 12

        # The height of the game is 960 pixels, if the player falls
        # down from the map.
        # This statement kills him.
        if self.rect.bottom >= 960:
            self.kill()

    def draw(self):
        x = 0

        # Draw the lives.
        for i in range(0, len(self.lives)):
            Artist.draw_textures(self.lives[i], (x, 50))

            # Set the space between the lives.
            x += 55

        # This method draws the player.
        # It needs an image and a list of integers.
        # The list of integers is the rect variable, this list holds
        # the x, y, width and height of the player.
        # The image is calculated by the PlayerAnimation class,
        # what it does is explained there.
        Artist.draw_textures(self.animation.update(), self.rect)

        # These four method are the images for the collider.
        # Because its hard to explain, its described in our report.
        Artist.draw_textures(self.player_under_image.image,
                             self.player_under_image.rect)
        Artist.draw_textures(self.player_up_image.image,
                             self.player_up_image.rect)
        Artist.draw_textures(self.player_left_image.image,
                             self.player_left_image.rect)
        Artist.draw_textures(self.player_right_image.image,
                             self.player_right_image.rect)

    def jump(self):
        # Set the player_snow and player_on_ice to false when te
        # player jumps.
        # Because the player is in the air.
        self.player_on_snow = False
        self.player_on_ice = False

        # Set the speed back to 4. Four is the normal speed.
        self.set_sliding(4)

        # This fixes the bug that you get double jump sounds when
        # you die.
        # Because when you die you get a jump sound and when you jump
        # you get a jump sound.
        # pygame.mixer.get_busy() checks if the mixer is busy.
        # If not, play the jump sound.
        if not pygame.mixer.get_busy():
            self.jump_sound.play()

        self.y_speed = 10
        self.jumps_remaining -= 1

    def basic_movement(self):
        # If the camera isn't shifting, we use the x axis on the player.
        # And we add the player's x with the player's x_speed
        # every frame.
        # So the player can move.
        if not self.is_shifting:
            self.rect.x += self.x_speed

        # Increase the player's y with the y_speed every frame.
        # So the player can move on the y axis.
        self.rect.y -= self.y_speed

        # Set the x_speed back to zero after we added the x_speed.
        self.x_speed = 0

    def gravity(self):
        self.y_speed -= 0.4

    def kill(self):
        if not self.dead:
            self.states = PlayerDieState(self)
            self.level_state_manager.player_health -= 1

    def get_player_x_speed(self):
        return self.x_speed

    def get_player_x(self):
        return self.rect.x

    # Set the speed on which the player should be sliding.
    # It's used when the player is standing on snow or ice
    # to make a sliding effect.
    def set_sliding(self, speed):
            self.states.player_slide_speed = speed
