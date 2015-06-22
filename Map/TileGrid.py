from Map.Tile import *
from Sprite.SpriteSheet import *
from Helpers.Artist import *

class TileGrid(SpriteSheet):

    map_group = pygame.sprite.Group()
    background_image = None
    rows = 60
    collums = 12

    shift_speed = 8.0

    def __init__(self, level_path, sprite_path):
        super(TileGrid, self).__init__(sprite_path)

        file = open(level_path)

        self.background_image = pygame.image.load("../Data/Levels/BackgroundEen.png").convert()

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
        Artist.get_display().blit(self.background_image, [0, 0])
        self.map_group.draw(Artist.get_display())

    def shift_map(self, player_x_speed):
        for sprite in self.map_group:
            sprite.shift_x(player_x_speed)
            #sprite.shift_x(round(player_x_speed / self.shift_speed)

    @staticmethod
    def get_group():
        return TileGrid.map_group



'''
public class Camera
{
	public static void setCamera(float playerX, float playerY)
	{
		glMatrixMode(GL_PROJECTION);
		glLoadIdentity();

		if(playerX < WIDTH/2)
		{
			glOrtho(0, WIDTH, HEIGHT, 0, -1, 1);
		}
		else if(playerX > TOTALWIDTH - (WIDTH / 2))
		{
			glOrtho(TOTALWIDTH - WIDTH, TOTALWIDTH, HEIGHT, 0, -1, 1);
		}
		else
		{
			glOrtho(playerX - (WIDTH / 2), playerX + (WIDTH / 2), HEIGHT, 0, -1, 1);
		}

		glMatrixMode(GL_MODELVIEW);
	}
}
'''