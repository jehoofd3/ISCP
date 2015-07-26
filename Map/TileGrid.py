from Map.Tile import *
from Sprite.ImageLoader import *
from Helpers.Artist import *

class TileGrid(ImageLoader):

    map_group = pygame.sprite.Group()
    background_image = None
    rows = 60
    columns = 12
    shift_speed = 8.0

    x_start = 0
    x_start_shift_map = 0
    display = Artist.get_display()

    def __init__(self, level_list):
        self.map_group.empty()

        help = 0
        for i in range(self.columns):
            for j in range(self.rows):
                image_type = ''
                imageNumber = level_list[help]
                help += 1

                for x in range(80, 83):
                    if imageNumber == x:
                        image_type = 'Lava'

                for x in range(83, 86):
                    if imageNumber == x:
                        image_type = 'Water'

                for x in range(117, 135):
                    if x == 118 or x == 119:
                        continue
                    elif imageNumber == x:
                        image_type = 'Snow'

                for x in range(156, 172):
                    if imageNumber == x:
                        image_type = 'Ice'

                if imageNumber == 114:
                    image_type = 'Exit'

                if imageNumber == -1 or imageNumber == 0:
                    pass
                else:
                    self.map_group.add(Tile(j * 64, i * 64, super(TileGrid, self).get_image(0, (imageNumber - 1) * 64, imageNumber), image_type))

    def run(self):
        pass

    def draw(self):
        self.map_group.draw(Artist.get_display())

    def shift_map(self, player_x_speed):
        self.x_start_shift_map += player_x_speed
        for sprite in self.map_group:
            sprite.shift_x(player_x_speed)

    @staticmethod
    def get_group():
        return TileGrid.map_group

    def set_x_start_shift_map(self, player_spawn_x):
        self.x_start_shift_map = player_spawn_x