from Helpers.Artist import *
from Enemy.Bullet.BulletExplosionState import *
from BulletFollowState import *
from Helpers.DatabaseReceiver import *
import random


class Bullet(object):
    # The states variable is a list to store the states of the bullet.
    states = None

    # This method is called when an bullet is made.
    # It takes three variables, two integers and a boolean.
    # The integers are the x and y position of the bullet.
    # The boolean left_right is used for the direction of the bullet.
    def __init__(self, x, y, left_right):
        # The variable img contains the image of the bullet.
        # The image is stored in the database, so it used a method in,
        # the DatabaseReceiver class.
        self.img = DatabaseReceiver.get_bullet_img("bullet")

        # self.rect is a list of four ints x, y, width and height.
        # The draw method in Artist needs this data to draw the image properly.
        # The get_rect() method on the image only places the width and height,
        # in the rect variable.
        self.rect = self.img.get_rect()

        # The rect.x variable is a method to change the x variable in rect.
        # Because the image doesn't have a x and y in the beginning, it has to,
        # be changed in this way.
        self.rect.x = x

        # The rect.y variable is a method to change the y variable in rect.
        # Because the image doesn't have a x and y in the beginning, it has to,
        # be changed in this way.
        self.rect.y = y

        # The integer x_speed is used for the movement of the bullet.
        # By default it is set on zero
        self.x_speed = 0

        # The y_speed is used for the movement on the y axis.
        # The value is a random number between one and six.
        # This makes every bullet move different.
        self.y_speed = random.randint(1, 6)

        # This speed variable is a integer and is used to move the,
        # bullet every frame eight pixels.
        # It is used for the x_speed and the y_speed.
        self.speed = 8

        # The active boolean is a variable that tells the collider if the,
        # bullet is active (dead or alive).
        self.active = True

        # This booleans tells if the bullet needs to move left or right.
        self.left_right = left_right

        # The angle variable is used to calculate the angle of the bullet.
        self.angle = 0

        # When the bullet is created, this line of code pushes a state.
        # In this case it is the BulletFollowState.
        self.states = BulletFollowState(self)

    def update(self):
        # Call the update method of the current state.
        self.states.update()

        # This if statement calculate the angle of the bullet.
        # If the y speed is greater than zero, execute the code.
        if self.y_speed > 0:
            # The angle will be corrected with the y speed of the bullet
            self.angle = 360 - self.y_speed
        else:
            # The angle will be corrected with the y speed of the bullet.
            self.angle = self.y_speed

    def draw(self):
        # It the x speed of the bullet is higher than zero, execute the code.
        if self.x_speed > 0:
            # The Artist class has a method that draws images in an angle.
            # The bullet calls the method and gives three variables.
            # The image of the bullet, a list with the x, y width and height,
            # (rect) and the angle.
            Artist.rotate_img(self.img, self.rect, self.angle)
        else:
            # It the x speed is smaller than zero it is moving to,
            # the left side.
            # By adding 180 to the angle, it rotates 180 degree.
            Artist.rotate_img(self.img, self.rect, self.angle + 180)

    # This method controls the basic movement of the bullet.
    def basic_movement(self):
        # When he moves on the x axis the value of x_speed changes, then that,
        # value is added of extracted with the x position of the bullet,
        # this position is stored,
        # in the rect list (rect.x).
        self.rect.x += self.x_speed

        # The y position of the enemy uses the same technique as the x,
        # position.
        self.rect.y -= self.y_speed

        # It is important to set the x_speed back to zero, or else the bullet,
        # will never stop,
        # moving on the x axis.
        self.x_speed = 0

    # This method is used to define the gravity.
    def gravity(self):
        # The y_speed of the bullet will be higher so he falls faster to,
        # the ground.
        self.y_speed -= 0.1

    # This method is called when the bullet collides with another object.
    def explode(self):
        # This line of code pushes the BulletExplosionState.
        self.states = BulletExplosionState(self)

    # Richard Jongenburger crap code
    def move_with_map(self, shift_x):
        self.rect.x -= shift_x
