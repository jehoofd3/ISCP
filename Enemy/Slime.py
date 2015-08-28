from Enemy import *
from SlimeNormalState import *
from Snake import *


class Slime(Enemy):
    # These four variables are used to store the images.
    # w_l and w_r are lists the other two are objects.
    w_l, w_r, d_l, d_r = [None, None], [None, None], None, None

    # The slime shoots snakes in his normal state.
    # He needs a list to store them.
    snake_list = []

    # This variable is used by the collider to check if the slime has
    # shoot a new snake.
    # If he shoots one, this number add up.
    snake_hulp = 0

    def __init__(self, x, y):
        # Creating enmpy variables.
        self.snake_list = []
        self.snake_hulp = 0
        self.w_l = []
        self.w_r = []

        # This variables are images and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.OB = DatabaseReceiver.get_enemy_img("Slime", "Slime_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Slime", "Slime_LR")

        # These methods are stored in the DatabaseReceiver class,
        # all the images are stored in the database.
        # These methods get them from the database and add them to
        # the image lists.
        self.w_l.append(DatabaseReceiver.get_enemy_img("Slime", "slime_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Slime", "slime_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Slime", "slime_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Slime", "slime_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Slime", "slime_d")
        self.d_r = DatabaseReceiver.get_enemy_img("Slime", "slime_d")

        # This game is object oriented and the class extends from Enemy
        # so its required
        # to call the super class by using the super() method.
        super(Slime, self).__init__(x, y, 0, self.w_l, self.w_r, self.d_l,
                                    self.d_r, self.OB, self.LR)

        # When the fly is created this line of code changes the states
        # object in enemy into SlimeNormalState.
        self.states = SlimeNormalState(self)

    # This method adds a snake to the snake_list.
    # It needs two integers, the x and y position.
    def add_snake(self, x, y):
        # This line of code adds the snake to the list.
        self.snake_list.append(Snake(x, y, 0))

    # This method returns a snake back to its caller.
    # With variable index, the caller can get a specific index
    # of the list.
    def get_snake(self, index):
        return self.snake_list[index]
