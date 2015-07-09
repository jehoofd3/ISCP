from EnemyState import *
from FishJumpState import *
import time


class FishNormalState(EnemyState):

    def __init__(self, enemy):
        super(FishNormalState, self).__init__(enemy)
        
    def run(self):
        self.enemy.rect.y = self.enemy.start_y
        self.enemy.ySpeed = 0
        self.right = True
        self.left = False
        self.start_time = time.time()
        self.switch_time = 7

    def update(self):
        self.enemy.block_u = False
        self.enemy.basic_movement()
        self.current_time = time.time()

        if self.enemy.rect.x <= self.enemy.start_x:
            self.right = True
            self.left = False

        if self.enemy.rect.x > self.enemy.start_x + self.enemy.range:
            self.right = False
            self.left = True

        if self.left:
            self.enemy.xSpeed -= self.enemy.speed
        if self.right:
            self.enemy.xSpeed += self.enemy.speed

        if self.current_time - self.start_time >= self.switch_time:
            self.enemy.states = [FishJumpState(self.enemy)]


    def draw(self):
        pass