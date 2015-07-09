from EnemyState import *
import FishNormalState as fns


class FishJumpState(EnemyState):

    def __init__(self, enemy):
        super(FishJumpState, self).__init__(enemy)

    def run(self):
        self.enemy.ySpeed = 20

    def update(self):
        self.enemy.block_u = False
        self.enemy.basic_movement()
        self.enemy.gravity()

        if self.enemy.rect.y >= self.enemy.start_y:
            self.enemy.states = [fns.FishNormalState(self.enemy)]

    def draw(self):
        pass