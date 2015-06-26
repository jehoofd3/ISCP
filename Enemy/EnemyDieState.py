from EnemyState import *



class EnemyDieState(EnemyState):

    def __init__(self, enemy):
        super(EnemyDieState, self).__init__(enemy)
        self.enemy = enemy

    def run(self):
        self.enemy.dead = True

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)

    def draw(self):
        pass