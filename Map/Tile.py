import pygame

# Author: Richard Jongenburger.


class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image, image_type):

        # To initialize pygame's Sprite class.
        pygame.sprite.Sprite.__init__(self)

        # Set the image.
        self.image = image

        # Get a rectangle object of the image.
        # It consist of (left, right, width, height).
        #
        # The rectangle that is returned by
        # using get_rect will always be (0, 0, image_width, image_height).
        self.rect = self.image.get_rect()

        # Set the x and y coordinate of the tile.
        self.rect.x = x
        self.rect.y = y

        # Set the type of the image.
        self.image_type = image_type

    # Move the x coordinate of the tile.
    # The x_speed is the number of units it should move.
    def shift_x(self, x_speed):
        self.rect.x -= x_speed

    def get_x(self):
        return self.x
