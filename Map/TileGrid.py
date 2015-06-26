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

    def __init__(self, level_path):
        file = open(level_path)
        self.map_group.empty()
        self.background_image = pygame.image.load("../Data/Levels/BackgroundEen.png")

        for i in range(self.columns):
            for j in range(self.rows):
                imageNumber = int(file.next())
                if imageNumber == -1 or imageNumber == 0:
                    pass
                else:
                    self.map_group.add(Tile(j * 64, i * 64, super(TileGrid, self).get_image(0, (imageNumber - 1) * 64, imageNumber), imageNumber))

    def run(self):
        pass

    def draw(self):
        self.map_group.draw(Artist.get_display())

    def shift_map(self, player_x_speed):
        self.x_start_shift_map += player_x_speed
        for sprite in self.map_group:
            sprite.shift_x(player_x_speed)
            #sprite.shift_x(round(player_x_speed / self.shift_speed)

    @staticmethod
    def get_group():
        return TileGrid.map_group

    def set_x_start_shift_map(self, player_spawn_x):
        self.x_start_shift_map = player_spawn_x