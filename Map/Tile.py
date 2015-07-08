import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image, image_type):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_type = image_type

    def shift_x(self, x_speed):
        self.rect.x -= x_speed

    def get_x(self):
        return self.x
