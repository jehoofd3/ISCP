from Player.Player import *
from Map.TileGrid import *
from GameState import *
__metaclass__ = type


class Level1State(GameState):

    map = TileGrid("../Levels/ProjectEen.txt", "../Images/Sprite1.png")
    player = Player(10, 10, "../Images/p2_front.png")

    def __init__(self, gsm):
        super(Level1State, self).__init__(gsm)

    def run(self):
        print "Lvl1Run"

    def update(self):
        self.player.update()
       # collision = pygame.sprite.groupcollide(self.player.get_group(), self.map.get_group(), False, False)
       # hit = pygame.sprite.spritecollide(self.player, self.map.get_group(), False)


        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self.player, self.map.get_group(), False)
        for block in block_hit_list:

            '''
            if self.player.xSpeed > 0:
                self.player.rect.right = block.rect.left
                print "a"
            elif self.player.xSpeed < 0:
                self.player.rect.left = block.rect.right
                print "b"
            '''

            self.player.rect.bottom = block.rect.top

            '''
            if self.player.ySpeed > 0:
                self.player.rect.top = block.rect.bottom
            elif self.player.ySpeed < 0:
                self.player.rect.bottom = block.rect.top
            '''



    def draw(self):
        self.map.draw()
        self.player.draw()