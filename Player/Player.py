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

    # The four booleans block_u, block_d, block_r and block_l indicates if the,
    # player is colliding with other objects.
    # These variables are set true or false by the collider.
    # The player uses it to see if it can move a particular position.
    block_u, block_d, block_r, block_l = None, None, None, None

    # The dead boolean is False if the player is alive and True if it is dead,
    # an can be set by the collider or the player himself.
    dead = None

    # Richard Jongenburger
    canGoRight = False
    canGoLeft = False
    collision_under = False
    collision_up = False

    # Richard Jongenburger
    half_screen_width = Artist.get_half_screen_width()
    face_direction = 'Right'

    # The jumps_remaining variable is an integer and controls the player's,
    # jumps.
    # He can only jump one time.
    jumps_remaining = 0

    # This variable is an integer and used to let the player move on the,
    # x axis.
    x_speed = 0

    # Richard Jongenburger
    x_speed_standing_still = 0

    y_speed = 0

    # Richard Jongenburger
    start_x = 0
    start_y = 0
    is_shifting = False
    sliding = False

    # Richard Jongenburger
    health_image_full = DatabaseReceiver.get_player_img("Health_Full")
    health_image_empty = DatabaseReceiver.get_player_img("Health_Empty")

    # Richard Jongenburger
    lives = ['', '', '']

    level_state_manager = None

    # These variables are used to calculate the collision.
    # It is hard to explain in comments.
    # We explain it in the report.
    player_under_image = None
    player_up_image = None
    player_left_image = None
    player_right_image = None

    # Richard Jongenburger
    jump_sound = None

    # Richard Jongenburger
    player_on_snow = False
    player_on_ice = False

    def __init__(self, x, y, level_state_manager):
        # Richard Jongenburger
        self.level_state_manager = level_state_manager
        for i in range(0, len(self.lives)):
            if i <= (self.level_state_manager.player_health - 1):
                self.lives[i] = self.health_image_full
            else:
                self.lives[i] = self.health_image_empty

        # Richard Jongenburger ik weet niet wat dit doet, heb jij dit gemaakt?
        pygame.sprite.Sprite.__init__(self)

        # self.rect is a list of four ints x, y, width and height.
        # The draw method in Artist needs this data to draw the image properly.
        # The get_rect() method on the image only places the width and height,
        # in the rect variable.
        self.rect = DatabaseReceiver.get_player_img("stand_r").get_rect()

        # The rect.x variable is a method to change the x variable in rect.
        # Because the image doesn't have a x and y in the beginning, it has to,
        # be changed in this way.
        self.rect.x = x

        # The rect.y variable is a method to change the y variable in rect.
        # Because the image doesn't have a x and y in the beginning, it has to,
        # be changed in this way.
        self.rect.y = y

        # The start_x and start_y are integers used to set the player,
        # back to his original position after he died.
        self.start_x = x
        self.start_y = y

        # Richard Jongenburger
        self.jump_sound = pygame.mixer.Sound('../Data/Music/Levels/Jump.wav')

        # The speed integer is used to calculate the speed of the player,
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

        # When the player is created this line of code changes the states,
        # object into PlayerNormalState.
        self.states = PlayerNormalState(self)

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_under_image = pygame.sprite.Sprite()
        self.player_under_image.image = DatabaseReceiver.get_player_img("OB")
        self.player_under_image.rect = self.player_under_image.image.get_rect()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_up_image = pygame.sprite.Sprite()
        self.player_up_image.image = DatabaseReceiver.get_player_img("OB")
        self.player_up_image.rect = self.player_up_image.image.get_rect()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_left_image = pygame.sprite.Sprite()
        self.player_left_image.image = DatabaseReceiver.get_player_img("LR")
        self.player_left_image.rect = self.player_left_image.image.get_rect()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_right_image = pygame.sprite.Sprite()
        self.player_right_image.image = DatabaseReceiver.get_player_img("LR")
        self.player_right_image.rect = self.player_right_image.image.get_rect()

    def run(self):
        # This line of code calls the run method in the state.
        self.states.run()

    def update(self):
        # This line of code calls the update method in the state.
        self.states.update()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_under_image.rect.x = self.rect.x + 10
        self.player_under_image.rect.y = self.rect.y + 94

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_up_image.rect.x = self.rect.x + 10
        self.player_up_image.rect.y = self.rect.y - 1

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_left_image.rect.x = self.rect.x - 1
        self.player_left_image.rect.y = self.rect.y + 12

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.player_right_image.rect.x = self.rect.x + 70
        self.player_right_image.rect.y = self.rect.y + 12

        # The height of the game is 960 pixels, if the player falls down,
        # from the map.
        # This statement kills him.
        if self.rect.bottom >= 960:
            self.kill()

    def draw(self):
        x = 0
        for i in range(0, len(self.lives)):
            Artist.draw_textures(self.lives[i], (x, 50))
            x += 55

        # This method draws the player.
        # It needs an image and a list of integers.
        # The list of integers is the rect variable, this list holds the x, y,
        # width and height of the player.
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
        # Richard Jongenburger
        self.player_on_snow = False
        self.player_on_ice = False
        self.set_sliding(4)

        if not pygame.mixer.get_busy():
            self.jump_sound.play()

        # If the player jumps, 10 will be added to his y_speed.
        self.y_speed = 10

        # If the player jumps, the variable jumps_remaining is lowered,
        # by one, so it is zero and the player can't jump again.
        self.jumps_remaining -= 1

    def basic_movement(self):
        # Richard Jongenburger
        if not self.is_shifting:
            # When he moves on the x axis the value of x_speed changes,
            # then that value is added of extracted with the x,
            # position of the player this position is stored,
            # in the rect list (rect.x).
            self.rect.x += self.x_speed

        # The y position of the player uses the same technique as the x,
        # position.
        self.rect.y -= self.y_speed

        # It is important to set the x_speed back to zero, or else the enemy,
        # will never stop moving on the x axis.
        self.x_speed = 0

    # This method is used to define the gravity.
    def gravity(self):
        # The y_speed of the player will be higher so he falls faster to,
        # the ground.
        self.y_speed -= 0.4

    # This method is used to kill the player.
    def kill(self):
        if not self.dead:
            # When this method is called, the player will push,
            # the PlayerDieState
            self.states = PlayerDieState(self)

            # Richard Jongenburger
            self.level_state_manager.player_health -= 1

    # Richard Jongenburger
    def get_player_x_speed(self):
        return self.x_speed

    # Richard Jongenburger
    def get_player_x(self):
        return self.rect.x

    # Richard Jongenburger
    def set_sliding(self, speed):
            self.states.player_slide_speed = speed
