from Map.TileGrid import *
import LevelState
from Player.Player import *
from Collider.Collider import *
from Helpers.Artist import *
from MainMenu.MainMenu import *

class EndDemo(LevelState):

    background_image = pygame.image.load("../Data/Images/end_demo.png").convert()

    def __init__(self):
        pass

    def run(self):
        pass

    def update(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            pygame.quit()
            quit()

    def draw(self):
        Artist.get_display().blit(self.background_image, [0, 0])

