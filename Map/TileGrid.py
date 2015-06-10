from Map.Tile import *
from Sprite.SpriteSheet import *
from Helpers.Artist import *

class TileGrid(SpriteSheet):

    map_group = pygame.sprite.Group()
    rows = 60
    collums = 12

    def __init__(self, level_path, sprite_path):
        super(TileGrid, self).__init__(sprite_path)

        file = open(level_path)
        for i in range(self.collums):
            for j in range(self.rows):
                img = int(file.next())
                if img == -1 or img == 0:
                    pass
                else:
                    self.map_group.add(Tile(j * 64, i * 64, super(TileGrid, self).get_image(0, (img - 1) * 64, 64, 64)))

    def run(self):
        pass

    def draw(self):
        self.map_group.draw(Artist.get_display())

    @staticmethod
    def get_group():
        return TileGrid.map_group
