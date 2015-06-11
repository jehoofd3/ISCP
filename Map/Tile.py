import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def shift_x(self, x_speed):
        print x_speed
        self.rect.x -= x_speed
