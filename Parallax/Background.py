from Parallax import *


class Background(Parallax):

    # The constructor only needs one variable.
    # It's the image of the background.
    def __init__(self, image):
        # This game is object oriented and the class extends from Parallax,
        # so its required
        # to call the super class by using the super() method.
        super(Background, self).__init__(image, -200, 0)
