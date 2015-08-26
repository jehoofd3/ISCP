from EnemyState import *


class EnemyDieState(EnemyState):

    def __init__(self, enemy):
        # This game is object oriented and the class extends from EnemyState,
        # so its required
        # to call the super class by using the super() method.
        super(EnemyDieState, self).__init__(enemy)

        # This variable is the enemy , this game is a statemachine,
        # (explained in our report),
        # the enemy is passed by by the statemachine.
        # It is needed so the state can change the variables of the enemy
        self.enemy = enemy

        # The variable dead in enemy is set True.
        # The collider can now see that the enemy is dead.
        self.enemy.dead = True

    def update(self):
        # The state called the basic_movement and gravity method, so it can,
        #  move on both axis.
        self.enemy.basic_movement()
        self.enemy.gravity()

        # If the enemy is touching a Tile under him, this code will be execute.
        if self.enemy.block_d:

            # Because there is a Tile under the enemy, his y_speed will be,
            # set to zero.
            # The gravity will not work, so he stops falling down.
            self.enemy.y_speed = 0

            # Sometimes the enemy will float over the map when he touched a,
            # Tile this is because of some rounding differences.
            # The bottom (integer) of the enemy will be divided by the height,
            # of a Tile (64).
            # Because rect.bottom is an integer, python will automatically,
            # round the outcome.
            # When you multiple the outcome by 64 (Tile height),
            # the rounding differences will be corrected.
            # See the report for a detailed explanation.
            self.enemy.rect.bottom = ((self.enemy.rect.bottom / 64) * 64)
