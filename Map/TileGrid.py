from Map.Tile import *
from Sprite.SpriteSheet import *
from Helpers.Artist import *

class TileGrid(SpriteSheet):

    map_group = pygame.sprite.Group()
    rows = 60 #len(map)
    collums = 12 #len(map[0])

    def __init__(self, level_path, sprite_path):
        #Set sprite path in spritesheet
        super(TileGrid, self).__init__(sprite_path)
        self.level_path = level_path

        self.create_map()

    def run(self):
        pass

    def draw(self):
        self.map_group.draw(Artist.get_display())

    def create_map(self):
        file = open(self.level_path)

        for i in range(self.collums):
            for j in range(self.rows):
                img = int(file.next())
                if (img == -1 or img == 0):
                    pass
                else:
                    self.map_group.add(Tile(j * 64, i * 64, super(TileGrid, self).get_image(0, (img - 1) * 64, 64, 64)))

    @staticmethod
    def get_group():
        return TileGrid.map_group
