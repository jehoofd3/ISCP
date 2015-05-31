from Map.Tile import *
from Helpers.Artist import *
from Sprite.SpriteSheed import *

class TileGrid(SpriteSheet):
    map_group = pygame.sprite.Group()
    rows = 60 #len(map)
    collums = 12 #len(map[0])

    def __init__(self, level_path, sprite_path):
        super(TileGrid, self).__init__(sprite_path)

        '''
        for i in range(self.collums):
            for j in range(self.rows):
                self.map_group.add(Tile(j*64, i*64, super(TileGrid, self).get_image(128, 0, 64, 64)))
        '''
        for i in range(9):
            self.map_group.add(Tile(i*64, 704, super(TileGrid, self).get_image(128, 0, 64, 64)))
        self.map_group.add(Tile(512, 640, super(TileGrid, self).get_image(128, 0, 64, 64)))

    def draw(self):
        self.map_group.draw(Artist.get_display())

    def get_group(self):
        return self.map_group
