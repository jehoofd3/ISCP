from Parallax import *

class Image(Parallax):

    def __init__(self, image_path, x, y):
        super(Image, self).__init__(image_path, x, x)
