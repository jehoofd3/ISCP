from Parallax import *

class Image(Parallax):

    def __init__(self, image, x, y, speed):
        self.speed = speed
        super(Image, self).__init__(image, x, y)

    def update(self, x, y, player_x):
        super(Image, self).update(x, y, player_x)
        if x >= 0:
            self.x -= self.speed
        else:
            self.x += self.speed
