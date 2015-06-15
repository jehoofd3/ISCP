from EnemyState import *
import TankNormalState as tns
import time


class TankShootState(EnemyState):

    def __init__(self, enemy):
        super(TankShootState, self).__init__(enemy)

    def run(self):
        self.enemy.speed /= 2
        self.start_time = time.time()
        self.shoot_time = 2

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()
        self.current_time = time.time()

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 2

        if self.enemy.left_right:
            self.enemy.xSpeed += self.enemy.speed
        else:
            self.enemy.xSpeed -= self.enemy.speed

        # Code om de kogel af te vuren
        if self.current_time >= self.start_time + self.shoot_time:
            # zorgen dat de bullet aan het einde van de loop afgeschoten wordt
            if self.enemy.xSpeed < 0:
                self.enemy.add_bullet(self.enemy.rect.x, self.enemy.rect.y)

            self.start_time = time.time()

     #   if not self.enemy.follow:
      #      self.enemy.states = [tns.TankNormalState(self.enemy)]

    def draw(self):
        pass