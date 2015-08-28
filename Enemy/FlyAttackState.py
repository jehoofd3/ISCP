from EnemyState import *
import FlyNormalState as fns


class FlyAttackState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from
        # EnemyState so its required
        # to call the super class by using the super() method.
        super(FlyAttackState, self).__init__(enemy)

        # Multiple the speed of the fly by 1.2, so the fly moves faster
        # when he is chasing the player.
        self.enemy.speed *= 1.2

    def update(self):
        # The state called the basic_movement and gravity method
        # so it can move on both axis.
        self.enemy.basic_movement()
        self.enemy.gravity()

        # If the enemy is touching a Tile under him, this code
        # will be execute.
        if self.enemy.block_d:
            # Because there is a Tile under the enemy, his y_speed will
            # be set to zero.
            # The gravity will not work, so he stops falling down.
            self.enemy.y_speed = 0

            # Sometimes the enemy will float over the map when he
            # touched a Tile this is because of some
            # rounding differences.
            # The bottom (integer) of the enemy will be divided by the
            # height of a Tile (64).
            # Because rect.bottom is an integer, python will
            # automatically round the outcome.
            # When you multiple the outcome by 64 (Tile height) the
            # rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)

            # Change the value of jumps_remaining so the enemy can
            # jump again
            self.enemy.jumps_remaining = 1

        # When the fly doesn't touche the ground, its jumps so he
        # doesn't kill himself easily.
        else:
            self.enemy.jump()

        # When the variable left_right is True, add the speed to the
        # value of the fly's x position.
        # This code lets the fly follow the player.
        if self.enemy.left_right:
            self.enemy.x_speed += self.enemy.speed
        else:
            self.enemy.x_speed -= self.enemy.speed

        # Set the x speed of the fly to zero if he touches a tile on
        # the left or right side and let him jump.
        # This lets the fly jump over tile.
        if self.enemy.block_l or self.enemy.block_r:
            self.enemy.x_speed = 0
            self.enemy.jump()

        # If the boolean follow in the enemy class is False, change the
        # state back to FlyNormalState.
        # This variable is changed by the collider is the enemy is out
        # of range (collider.range, not enemy.range).
        if not self.enemy.follow:
            self.enemy.states = fns.FlyNormalState(self.enemy)
