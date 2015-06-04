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
        self.create_map()

    def run(self):
        pass

    def draw(self):
        self.map_group.draw(Artist.get_display())

    def create_map(self):
        for i in range(9):
            self.map_group.add(Tile(i*64, 704, super(TileGrid, self).get_image(128, 0, 64, 64)))

        self.map_group.add(Tile(512, 640, super(TileGrid, self).get_image(128, 0, 64, 64)))
        self.map_group.add(Tile(256, 448, super(TileGrid, self).get_image(128, 0, 64, 64)))
        self.map_group.add(Tile(0, 640, super(TileGrid, self).get_image(128, 0, 64, 64)))

    @staticmethod
    def get_group():
        return TileGrid.map_group