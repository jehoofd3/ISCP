from EnemyState import *
import time


class SlimeNormalState(EnemyState):

    def __init__(self, enemy):
        super(SlimeNormalState, self).__init__(enemy)

    def run(self):
        self.start_time = time.time()
        self.shoot_time = 3

    def update(self):
        self.current_time = time.time()
        self.enemy.xSpeed = 5

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

        # Code om de snake af te vuren
        if self.current_time >= self.start_time + self.shoot_time:
            self.enemy.add_snake(self.enemy.rect.x, self.enemy.rect.y)
            self.start_time = time.time()

    def draw(self):
        pass