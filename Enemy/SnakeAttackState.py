from EnemyState import *


class SnakeAttackState(EnemyState):

    def __init__(self, enemy):
        super(SnakeAttackState, self).__init__(enemy)

    def run(self):
        pass

    def update(self):
        self.enemy.basic_movement()
        self.enemy.gravity()

        if self.enemy.l_r:
            self.enemy.xSpeed += self.enemy.speed
        else:
            self.enemy.xSpeed -= self.enemy.speed

        if self.enemy.block_d:
            self.enemy.ySpeed = 0
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
            self.enemy.jumpsRemaining = 1
        else:
            self.enemy.jump()

        if self.enemy.block_l:
            self.enemy.xSpeed = 0
            self.enemy.rect.x += 1

        if self.enemy.block_r:
            self.enemy.xSpeed = 0
            self.enemy.rect.x -= 1

    def draw(self):
        pass