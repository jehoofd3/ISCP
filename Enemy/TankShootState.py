from EnemyState import *
from TankNormalState import *
import time


class TankShootState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from
        # EnemyState so its required to call the super
        # class by using the super() method.
        super(TankShootState, self).__init__(enemy)

        # Multiple the speed of the tank by 1.2, so the tank moves
        # faster when he is chasing the player.
        self.enemy.speed *= 1.2

        # This boolean lets the tank shoot when he enters this state.
        # Without waiting two seconds.
        self.shoot_first = True

        # This variable is the start time of the frame
        # It is used to shoot a bullet.
        self.start_time = time.time()

        # This variable is used to set the amount of seconds to
        # shoot a bullet.
        self.shoot_time = 2

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
            # The bottom (integer) of the enemy will be
            # divided by the height of a Tile (64).
            # Because rect.bottom is an integer, python will
            # automatically round the outcome.
            # When you multiple the outcome by 64 (Tile height)
            # the rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)

            # Change the value of jumps_remaining so the enemy
            # can jump again
            self.enemy.jumps_remaining = 1

        # When the tank doesn't touche the ground, its jumps so he
        # doesn't kill himself easily.
        else:
            self.enemy.jump()

        # When the variable left_right is True, add the speed to the
        # value of the tank's x position.
        # This code lets the tank follow the player.
        if self.enemy.left_right:
            self.enemy.x_speed += self.enemy.speed
        else:
            self.enemy.x_speed -= self.enemy.speed

        # Set the x speed of the tank to zero if he touches a tile on
        # the left or right side and let him jump.
        # This lets the tank jump over tile.
        if self.enemy.block_l or self.enemy.block_r:
            self.enemy.x_speed = 0
            self.enemy.jump()

        # If the boolean shoot_first is True, shoot a bullet, and change
        # the variable to False.
        # This makes the tank shoot automatically on the
        # start of this state.
        if self.shoot_first:
            self.shoot()
            self.shoot_first = False

        # This method checks if the two seconds are over to shoot
        # a bullet.
        # The time.time() method gets the current time.
        # If this float minus the variable start_time is greater or
        # equal than switch_time is shoots the bullet.
        # This makes it shoot every two seconds.
        if time.time() >= self.start_time + self.shoot_time:
            self.shoot()

        # If the boolean follow in the enemy class is Talse, change the
        # state back to TankNormalState.
        # This boolean is changed by the collider and lets the tank
        # unfollow the player.
        if not self.enemy.follow:
            self.enemy.states = TankNormalState(self.enemy)

    # This method is used in this class to shoot a bullet.
    def shoot(self):
        # When the x speed of the tank is less than 0, than the bullet
        # will fly to the left direction.
        if self.enemy.x_speed < 0:
            self.enemy.add_bullet(self.enemy.rect.x, self.enemy.rect.y, True)

        # Else the bullet will fly to the right direction.
        else:
            self.enemy.add_bullet(self.enemy.rect.x + self.enemy.rect.width,
                                  self.enemy.rect.y, False)

        # This line of code resets the timer, so the tank will shoot
        # after two seconds.
        self.start_time = time.time()
