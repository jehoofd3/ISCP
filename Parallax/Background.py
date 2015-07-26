from Parallax import *


class Background(Parallax):

    def __init__(self, image, x, y):
        super(Background, self).__init__(image, -200, y)
