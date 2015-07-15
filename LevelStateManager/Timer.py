from Helpers.Artist import *

class Timer:

    numbers = []

    def __init__(self):
        for x in range(0, 9):
            self.numbers.append(pygame.image.load("../Data/Images/hud_" + str(x) + ".png").convert_alpha())

    def update(self):
        pass

    def draw(self):
        Artist.draw_textures(self.numbers[0], (700, 60))
