from EnemyState import *
import time


class SlimeNormalState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from EnemyState,
        # so its required to call the super class by using the super() method.
        super(SlimeNormalState, self).__init__(enemy)

        # This variable is the start time of the frame,
        # It is used to shoot a slime.
        self.start_time = time.time()

        # This variable is used to set the amount of seconds to,
        # shoot a slime
        self.shoot_time = 3

    def update(self):
        # The slime doesn't move on the x axis so it doesn't call the,
        # basic_movement() method but it has to fal to the ground.
        # So this line of code lets the slime fall to the ground
        self.enemy.rect.y -= self.enemy.y_speed
        self.enemy.gravity()

        # The slime doesn't move, but the x_speed need to be higher than,
        # zero to change the animations.
        self.enemy.x_speed = 5

        # If the enemy is touching a Tile under him, this code will be execute.
        if self.enemy.block_d:
            # Because there is a Tile under the enemy, his y_speed will be set,
            # to zero.
            # The gravity will not work, so he stops falling down.
            self.enemy.y_speed = 0

            # Sometimes the enemy will float over the map when he touched,
            # a Tile this is because of some rounding differences.
            # The bottom (integer) of the enemy will be divided by the height,
            # of a Tile (64).
            # Because rect.bottom is an integer, python will automatically,
            # round the outcome.
            # When you multiple the outcome by 64 (Tile height),
            # the rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)

        # This method checks if the three seconds are over to shoot a snake.
        # The time.time() method gets the current time.
        # If this float minus the variable start_time is greater or equal,
        # than switch_time shoot the snake.
        # This makes the slime shoot every three seconds.
        if time.time() >= self.start_time + self.shoot_time:
            self.enemy.add_snake(self.enemy.rect.x, self.enemy.rect.y)
            self.start_time = time.time()
