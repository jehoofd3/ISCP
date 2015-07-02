from Parallax import *


class Background(Parallax):

    def __init__(self, image_path, x, y):
        super(Background, self).__init__(image_path, -200, y)
