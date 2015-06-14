from EnemyState import *


class FishNormalState(EnemyState):

    def __init__(self, enemy):
        super(FishNormalState, self).__init__(enemy)
        
    def run(self):
        self.left = None
        self.right = None

    def update(self):
        self.enemy.basic_movement()

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

    def draw(self):
        pass