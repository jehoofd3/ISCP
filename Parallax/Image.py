from Parallax import *


class Image(Parallax):

    # This constructor takes four variables.
    # The image variable is an image.
    # The x and y variables are integers and
    # is used to set the location of the image.
    # The variable speed is an integer and used to
    # set the speed of the parallax effect.
    def __init__(self, image, x, y, speed):
        self.speed = speed

        # This game is object oriented and the class extends from
        # Parallax so its required
        # to call the super class by using the super() method.
        super(Image, self).__init__(image, x, y)

    # The update method uesd three variables.
    # x and y are integers used to set the location of the image.
    # The player is needed to check the location of the player in
    # the super class
    def update(self, x, y, player_x):
        # This line of code calls the update function of the
        # super class.
        super(Image, self).update(x, y, player_x)

        # This statement checks if the x is greather or equal than 0.
        if x >= 0:
            # The x minus the speed.
            # This moves the images to the left side.
            self.x -= self.speed
        else:
            # Add the speed to the x variable.
            # This moves the image to the right side.
            self.x += self.speed
