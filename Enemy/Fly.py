from FlyNormalState import *
from Enemy import *
from Helpers.DatabaseReceiver import *


class Fly(Enemy):
    # These four variables are used to store the images.
    # w_l and w_r are lists the other two are objects.
    w_l, w_r, d_l, d_r = [], [], None, None

    # This method is called when an enemy is made.
    # It takes four variables x, y and range are integers, they are explained,
    # in Enemy.
    def __init__(self, x, y, range):
        # Create two new empty lists.
        self.w_l = []
        self.w_r = []

        # This variables are images and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.OB = DatabaseReceiver.get_enemy_img("Fly", "Fly_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Fly", "Fly_LR")

        # These methods are stored in the DatabaseReceiver class, all the,
        # images are stored in the database.
        # These methods get them from the database and add them to the,
        # image lists.
        self.w_l.append(DatabaseReceiver.get_enemy_img("Fly", "l_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Fly", "l_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Fly", "r_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Fly", "r_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Fly", "d_l")
        self.d_r = DatabaseReceiver.get_enemy_img("Fly", "d_r")

        # This game is object oriented and the class extends from Enemy,
        # so its required
        # to call the super class by using the super() method.
        super(Fly, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l,
                                  self.d_r, self.OB, self.LR)

        # When the fly is created this line of code changes the states,
        # object in enemy into FlyNormalState.
        self.states = FlyNormalState(self)
