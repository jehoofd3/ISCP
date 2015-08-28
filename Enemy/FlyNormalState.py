from EnemyState import *
from FlyAttackState import *


class FlyNormalState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from
        # EnemyState so its required to call the super class by using
        # the super() method.
        super(FlyNormalState, self).__init__(enemy)

        # This booleans tells if the fish needs to move left or right.
        self.move_left_right = None

        # This line of code sets the speed back to the original speed.
        # When the fly changes his state to FlyAttackState
        # the speed changes.
        self.enemy.speed = self.enemy.start_speed

    def update(self):
        # The state called the basic_movement and gravity method,
        # so it can move on both axis.
        self.enemy.basic_movement()
        self.enemy.gravity()

        # This if statement checks if the x position of the fly
        # is smaller or equal than the x value on
        # creation (enemy.stary_x).
        if self.enemy.rect.x <= self.enemy.start_x:
            # If this statement is True, change move_left_right to False
            self.move_left_right = False

        # It the previous statement is False, this statement checks it
        # the x position of the fly is greater or equal than the x
        # value on creation plus the range of the fly.
        elif self.enemy.rect.x >= self.enemy.start_x + self.enemy.range:
            # If this statement is True, change move_left_right to True.
            self.move_left_right = True

        # This statement checks if the boolean move_left_right is True.
        if self.move_left_right:
            # If its True, lower the x position of the fly with
            # the speed
            # This makes the fly move in the left direction.
            self.enemy.x_speed -= self.enemy.speed
        else:
            # If its False, add the speed with the x position
            # of the fly.
            # This makes the fly move in the right direction.
            self.enemy.x_speed += self.enemy.speed

        # If the enemy is touching a Tile under him, this code will
        # be execute.
        if self.enemy.block_d:
            # Because there is a Tile under the enemy, his y_speed will
            # be set to zero.
            # The gravity will not work, so he stops falling down.
            self.enemy.y_speed = 0

            # Sometimes the enemy will float over the map when he
            # touched a Tile this is because of some rounding
            # differences.
            # The bottom (integer) of the enemy will be divided by the
            # height of a Tile (64).
            # Because rect.bottom is an integer, python will
            # automatically round the outcome.
            # When you multiple the outcome by 64 (Tile height)
            # the rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)

            # Change the value of jumps_remaining so the enemy
            # can jump again
            self.enemy.jumps_remaining = 1

        # When the fly doesn't touche the ground its jumps so he doesn't
        # kill himself.
        else:
            self.enemy.jump()

        # Set the x speed of the fly to zero if he touches a tile on the
        # left or right side and let him jump.
        # This lets the fly jump over tile.
        if self.enemy.block_l or self.enemy.block_r:
            self.enemy.x_speed = 0
            self.enemy.jump()

        # If the boolean follow in the enemy class is True, change the
        # state to FlyAttackState.
        # This boolean is changed by the collider and lets the fly
        # follow the player.
        if self.enemy.follow:
            self.enemy.states = FlyAttackState(self.enemy)
