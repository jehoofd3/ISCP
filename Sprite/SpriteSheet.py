
class SpriteSheet(object):

    def __init__(self, file_name):
            self.sprite_sheet = pygame.image_load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface[width, height].confert()

        image.blit(self.sprite_sheet, (0,0), (x, y,  width, height))

        image.set_colorkey((0, 0, 0))

        return image