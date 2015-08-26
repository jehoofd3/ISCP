from EnemyState import *
from FishJumpState import *
import time


class FishNormalState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from EnemyState,
        # so its required to call the super class by using the super() method.
        super(FishNormalState, self).__init__(enemy)

        # This line of code sets the y axis back to its original.
        self.enemy.rect.y = self.enemy.start_y

        # This variable sets the y_speed back to zero.
        # This is important so the fish stops falling down.
        self.enemy.y_speed = 0

        # This booleans tells if the fish needs to swim left or right.
        self.move_left_right = None

        # This variable is the start time of the frame,
        # because it is created in the init it only runs on creation,
        # of this state.
        # It is used to switch to the FishJumpState.
        self.start_time = time.time()

        # This variable is used to set the amount of seconds to switch,
        # to the FishJumpState.
        self.switch_time = 3

    def update(self):
        # The fish never touch a Tile because the collider doesn't see,
        # water or lava as ground.
        # Because of this the fis wil fall down the map,
        # and then the enemy kills itself (update method Enemy).
        # So by setting the block_u boolean on False, the fish thinks,
        # its always on the ground.
        self.enemy.block_u = False

        # The state called the basic_movement method, so it can move,
        # on both axis.
        self.enemy.basic_movement()

        # This if statement checks if the x position of the fish is smaller,
        # or equal than the x,
        # value on creation (enemy.stary_x).
        if self.enemy.rect.x <= self.enemy.start_x:
            # If this statement is True, change move_left_right to False
            self.move_left_right = False
            self.right = True
            self.left = False

        if self.enemy.rect.x > self.enemy.start_x + self.enemy.range:
            self.right = False
            self.left = True

        if self.left:
            self.enemy.x_speed -= self.enemy.speed
        if self.right:
            self.enemy.x_speed += self.enemy.speed

        # It the previous statement is False, this statement checks it the,
        # x position of the fish is,
        # greater or equal than the x value on creation plus the range of,
        # the fish.
        elif self.enemy.rect.x >= self.enemy.start_x + self.enemy.range:
            # If this statement is True, change move_left_right to True.
            self.move_left_right = True

        # This statement checks if the boolean move_left_right is True.
        if self.move_left_right:
            # If its True, lower the x position of the fish with the speed.
            # This makes the fish move in the left direction.
            self.enemy.x_speed -= self.enemy.speed
        else:
            # If its False, add the speed with the x position of the fish.
            # This makes the fish move in the right direction.
            self.enemy.x_speed += self.enemy.speed

        # This method checks if the three seconds are over to switch to,
        # the FishJumpState.
        # The time.time() method gets the current time.
        # If this float minus the variable start_time is greater or equal,
        # than switch_time start the FishJumpState.
        # This makes it jump every three seconds.
        if time.time() - self.start_time >= self.switch_time:
            # This line of code changes the object states to FishJumpState,
            # so it changes the state.
            self.enemy.states = FishJumpState(self.enemy)
