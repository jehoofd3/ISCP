from EnemyState import *
import FishNormalState as fns


class FishJumpState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from EnemyState,
        # so its required to call the super class by using the super() method.
        super(FishJumpState, self).__init__(enemy)

        # This varible changes the y speed of the fish on creation,
        # of this class.
        self.enemy.y_speed = 20

    def update(self):
        # The fish never touch a Tile because the collider doesn't see water,
        # or lava as ground.
        # Because of this the fis wil fall down the map,
        # and then the enemy kills itself (update method Enemy).
        # So by setting the block_u boolean on False, the fish thinks its,
        # always on the ground.
        self.enemy.block_u = False

        # The state called the basic_movement and gravity method,
        # so it can move on both axis.
        self.enemy.basic_movement()
        self.enemy.gravity()

        # When the current y position of the fish is greater or equal than,
        # the y position on creation.
        # Execute the code.
        if self.enemy.rect.y >= self.enemy.start_y:
            # This line of code changes the states object in enemy,
            # to FishNormalState.
            self.enemy.states = fns.FishNormalState(self.enemy)
