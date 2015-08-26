from SnakeAttackState import *
from Enemy import *
from Helpers.DatabaseReceiver import *


class Snake(Enemy):
    # These four variables are used to store the images.
    # w_l and w_r are lists the other two are objects.
    w_l, w_r, d_l, d_r = [], [], None, None

    # The boolean l_r is used by te snake to see witch side,
    # he needs to move to follow the player.
    # This variable is set by the collider.
    l_r = None

    def __init__(self, x, y, range):
        # Create two new empty lists.
        self.w_l = []
        self.w_r = []

        # This variables are images and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        self.OB = DatabaseReceiver.get_enemy_img("Snake", "Snake_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Snake", "Snake_LR")

        # These methods are stored in the DatabaseReceiver class, all the,
        # images are stored in the database.
        # These methods get them from the database and add them to the,
        # image lists.
        self.w_l.append(DatabaseReceiver.get_enemy_img("Snake", "l_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Snake", "l_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Snake", "r_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Snake", "r_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Snake", "d_l")
        self.d_r = DatabaseReceiver.get_enemy_img("Snake", "d_r")

        # This game is object oriented and the class extends from Enemy,
        # so its required
        # to call the super class by using the super() method.
        super(Snake, self).__init__(x, y, range, self.w_l, self.w_r,
                                    self.d_l, self.d_r, self.OB, self.LR)

        # When the snake is created this line of code changes the states,
        # object in enemy into SnakeAttackState.
        self.states = SnakeAttackState(self)
