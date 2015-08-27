import pygame
from Helpers.Artist import *
from FlyNormalState import *
from EnemyDieState import *
from Animation.EnemyAnimation import *


# Author: Jeroen van Ottelen.
class Enemy(object):
    # The states variable is a object to store the states of the enemy.
    states = None

    # The four booleans block_u, block_d, block_r and block_l indicates if the,
    # enemy is colliding with other objects.
    # These variables are set true or false by the collider.
    # The enemy uses it to see if it can move a particular position.
    block_u, block_d, block_r, block_l = None, None, None, None

    # The dead boolean is False if the enemy is alive and True if it is dead,
    # an can be set by the collider or the enemy himself.
    # The follow boolean is a variable used by the follow state of a enemy,
    # and is set by the collider.
    # If its True then the state of the enemy pushes its follow state,
    # (if it has one).
    # The follow state means that the enemy follows the player.
    # The left_right variable is a boolean set by the collider.
    # It controls the enemy's left or right movement.
    # When the enemy is in follow state, the collider checks if the player,
    # is left or right, of the enemy.
    # If the player is on the right side of the enemy, left_right is True.
    # So the enemy moves to the right side.
    # If the player is on the left side of the enemy, left_right is False.
    # So the enemy moves to the left side.
    dead, follow, left_right = False, False, None

    # The list bullet_list is a variable for the Tank.
    # The tank can shoot bullets, and these bullets need to be stored in a,
    # list so they can be updated and drawn.
    bullet_list = []

    # This is a variable that's needed to keep track on how much
    # X the enemies have moves since their spawn.
    # So everytime the enemies move, this variable will increase.
    # This is used by the camera.
    shift_x = 0

    # This method is called when an enemy is made.
    # It takes nine variables, the x and y are integers and used for the,
    # location of the enemy.
    # The variable range is a integer and tells the enemy how far he can move.
    # All the enemy's move left and right by default, this variable tells him,
    # how far he can go.
    # The variables walk_l and walk_r are lists of images.
    # These images makes the animation of the enemy if he walks left (walk_l),
    # or right (walk_r).
    # The variables dead_l and dead_r contains images of a dead enemy.
    # The variables OB and LR are images needed for the collider.
    # OB is 1 pixel in height, LR is 1 pixel wide.
    # When these images are colliding with the map or enemy, than the collider,
    # set an action.
    # Like kill the enemy, or set the enemy's y_speed on 0.
    # How this technique exactly works is described in our report.

    def __init__(self, x, y, range, walk_l, walk_r, dead_l, dead_r, OB, LR):
        # self.rect is a list of four ints x, y, width and height.
        # The draw method in Artist needs this data to draw the image properly.
        # The get_rect() method on the image only places the width and height,
        # in the rect variable.
        self.rect = walk_l[0].get_rect()

        # The rect.x variable is a method to change the x variable in rect.
        # Because the image doesn't have a x and y in the beginning, it has to,
        # be changed in this way.
        self.rect.x = x

        # The rect.y variable is a method to change the y variable in rect.
        # Because the image doesn't have a x and y in the beginning, it has to,
        # be changed in this way.
        self.rect.y = y

        # The variables x_speed and y_speed are integers used for the movement,
        # of the enemy.
        # They are by default 0.
        self.x_speed = 0
        self.y_speed = 0

        # This variable is to limit the amount of jumps of the enemy.
        # The enemy can only jump once, when he touched the ground this,
        # variable is set on 1.
        # If its not set on 0 bij default then the enemy jumps when he is,
        # created and not touching the ground.
        self.jumps_remaining = 0

        # This speed variable is a integer and is used to move the enemy every,
        # frame two pixels.
        # It is used for the x_speed and the y_speed.
        self.speed = 2

        # The start_speed is a integer used by some enemy's.
        # When a Fly changes to his AttackState, his speed changes.
        # When he goes back to his normal state, his speed is set back to the,
        # original value.
        self.start_speed = self.speed

        # The range variable is mentioned above.
        self.range = range

        # This variable is used for the range.
        # When the enemy is in his normal state he moves on the x axis, the,
        # range tells him how far he can go.
        # If the current X of the enemy is greater than the start_x + range,
        # then he needs to move back.
        # If the current X of the enemt is smaller than the start_x, he,
        # needs to move to the right side.
        self.start_x = x

        # Just like start_x, the start_y is used for the movement of the enemy.
        # The Fish jumps after a few seconds, when his current y position is,
        # greater than start_y his,
        # state changed back to its original.
        self.start_y = y

        # The range variable is mentioned above.
        self.bullet_list = []

        # Clear the states variable
        self.states = None

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.enemy_under_image = pygame.sprite.Sprite()
        self.enemy_under_image.image = OB
        self.enemy_under_image.rect = self.enemy_under_image.image.get_rect()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.enemy_up_image = pygame.sprite.Sprite()
        self.enemy_up_image.image = OB
        self.enemy_up_image.rect = self.enemy_up_image.image.get_rect()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.enemy_left_image = pygame.sprite.Sprite()
        self.enemy_left_image.image = LR
        self.enemy_left_image.rect = self.enemy_left_image.image.get_rect()

        # This variable is an image and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.enemy_right_image = pygame.sprite.Sprite()
        self.enemy_right_image.image = LR
        self.enemy_right_image.rect = self.enemy_right_image.image.get_rect()

        # This object is used to calculate the enemy images so it looks,
        # like an animation.
        # It needs the lists walk_l, and walk_r and the dead images.
        self.animation = EnemyAnimation(walk_l, walk_r, dead_l, dead_r)

    def update(self):
        # Call the update method of the current state.
        self.states.update()

        # Update the start_x with the shift_x every frame.
        # So we keep track how much the x is changed since the creation.
        self.start_x -= self.shift_x

        # These two line of code are changing the image used for the colission.
        # Because its hard to explain, its described in our report.
        self.enemy_under_image.rect.x = self.rect.x + 10
        self.enemy_under_image.rect.y = self.rect.y + self.rect.height + 1

        # These two line of code are changing the image used for the colission.
        # Because its hard to explain, its described in our report.
        self.enemy_up_image.rect.x = self.rect.x + 10
        self.enemy_up_image.rect.y = self.rect.y - 1

        # These two line of code are changing the image used for the colission.
        # Because its hard to explain, its described in our report.
        self.enemy_left_image.rect.x = self.rect.x - 1
        self.enemy_left_image.rect.y = self.rect.y

        # These two line of code are changing the image used for the colission.
        # Because its hard to explain, its described in our report.
        self.enemy_right_image.rect.x = self.rect.x + self.rect.width
        self.enemy_right_image.rect.y = self.rect.y

        # This if statement checks if there is a block on the left or,
        # right side of the enemy.
        # If there is a block, then he jumps.
        # Sometimes the enemy can't reach places because there is a block,
        # in his way.
        # This statement lets him jump, so he can continue his way.
        if self.block_l or self.block_r:
            self.jump()

        # The height of the game is 960 pixels, if the enemy falls down,
        # from the map.
        # This statement kills him.
        if self.rect.bottom >= 960:
            self.kill()

    def draw(self):
        # This method draws the enemy.
        # It needs an image and a list of integers.
        # The list of integers is the rect variable, this list holds the x, y,
        # width and height of the enemy.
        # The image is calculated by the EnemyAnimation class,
        # what it does is explained there.
        Artist.draw_textures(self.animation.update(self.x_speed, self.dead),
                             self.rect)

        # These four method are the images for the collider.
        # Because its hard to explain, its described in our report.
        Artist.draw_textures(self.enemy_under_image.image,
                             self.enemy_under_image.rect)
        Artist.draw_textures(self.enemy_up_image.image,
                             self.enemy_up_image.rect)
        Artist.draw_textures(self.enemy_left_image.image,
                             self.enemy_left_image.rect)
        Artist.draw_textures(self.enemy_right_image.image,
                             self.enemy_right_image.rect)

    # This method lets the enemy jump.
    def jump(self):
        # Because he can only jump one time, the variable jumps_remaining,
        # must be higher than one.
        if self.jumps_remaining > 0:
            # If the enemy jumps, 10 will be added to his y_speed.
            self.y_speed += 10
            # If the enemy jumps, the variable jumps_remaining is lowered,
            # by one, so it is zero and the enemy can't jump again.
            self.jumps_remaining -= 1

    # This method controls the basic movement of the enemy.
    def basic_movement(self):

        # When he moves on the x axis the value of x_speed changes, then that,
        # value is added of extracted with the x position of the enemy,
        # this position is stored,
        # in the rect list (rect.x).
        self.rect.x += self.x_speed

        # The y position of the enemy uses the same technique as the x,
        # position.
        self.rect.y -= self.y_speed

        # It is important to set the x_speed back to zero, or else the enemy,
        # will never stop moving on the x axis.
        self.x_speed = 0

        # Change the y_speed of the enemy if touches a tile with the top,
        # of the image.
        # This will make the enemy to fall down 3 pixels.
        # If the speed is set on zero, the enemy will stick at the bottom,
        # of a tile.
        if self.block_u:
            self.y_speed = - 3

    # This method is used to define the gravity.
    def gravity(self):
        # The y_speed of the enemy will be higher so he falls faster to,
        # the ground.
        self.y_speed -= 0.4

    # This method is used for killing the enemy.
    def kill(self):
        # When this method is called, the enemy will push its DieState
        self.states = EnemyDieState(self)

    # This method is needed for the camera.
    # It takes the shift_x as an argument.
    # That's the number of units the enemies will shift on the X as.
    # It makes it so when the player moves,
    # the enemies move with the payer speed.
    # Read in the camera class how the camera works.
    def move_with_map(self, shift_x):
        # Set the global shift_x variable to the local shift_x variable.
        self.shift_x = shift_x

        # Move the x of the enemies minus the shift_x variable.
        self.rect.x -= shift_x

        # Let all the bullets move as the player moves as well.
        for b in self.bullet_list:
            b.move_with_map(shift_x)
