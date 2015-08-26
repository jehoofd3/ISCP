from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from MainMenu.MainMenu import *
from Helpers.DatabaseReceiver import *

class EndDemo(LevelState):

    background_image = DatabaseReceiver.get_menu_img("End_Demo")

    def __init__(self):
        pass

    def run(self):
        pass

    def update(self):
        # This piece of code is used to quit the game when you pressed space.
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            pygame.quit()
            quit()

    def draw(self):
        # Draw the background to the screen.
        Artist.draw_textures(self.background_image, [0, 0])
