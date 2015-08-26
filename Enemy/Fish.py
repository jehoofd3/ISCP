from FishNormalState import *
from Enemy import *
from Helpers.DatabaseReceiver import *


class Fish(Enemy):
    # These four variables are used to store the images.
    # w_l and w_r are lists the other two are objects.
    w_l, w_r, d_l, d_r = [], [], None, None

    # This method is called when an enemy is made.
    # It takes four variables x, y and range are integers,
    # they are explained in Enemy.
    # The type variable is a String and can be Water of Lava.
    # If its Water, the images of the fish will be green.
    # It its Lava, the images of the fish will be red.
    def __init__(self, x, y, range, type):
        # Create two new empty lists.
        self.w_l = []
        self.w_r = []

        # This variables are images and it is used for the collision with,
        # other objects.
        # This technique is hard to explain without images so how exactly,
        # works is described in our report.
        self.OB = DatabaseReceiver.get_enemy_img("Fish", "Fish_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Fish", "Fish_LR")

        # If the variable type contains Water, add green fish images to,
        # the lists.
        if type == "Water":
            # These methods are stored in the DatabaseReceiver class, all the,
            # images are stored in the database.
            # These methods get them from the database and add them to,
            # the image lists.
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish",
                                                           "water_l_0"))
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish",
                                                           "water_l_1"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish",
                                                           "water_r_0"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish",
                                                           "water_r_1"))
            self.d_l = DatabaseReceiver.get_enemy_img("Fish",
                                                      "water_d_l")
            self.d_r = DatabaseReceiver.get_enemy_img("Fish",
                                                      "water_d_r")

        # If the type is not Water add red fish images to the lists.
        else:
            # These methods are stored in the DatabaseReceiver class, all the,
            #  images are stored in the database.
            # These methods get them from the database and add them to,
            # the image lists.
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish", "lava_l_0"))
            self.w_l.append(DatabaseReceiver.get_enemy_img("Fish", "lava_l_1"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish", "lava_r_0"))
            self.w_r.append(DatabaseReceiver.get_enemy_img("Fish", "lava_r_1"))
            self.d_l = DatabaseReceiver.get_enemy_img("Fish", "lava_d_l")
            self.d_r = DatabaseReceiver.get_enemy_img("Fish", "lava_d_r")

        # This game is object oriented and the class extends from Enemy,
        # so its required to call the super class by using the super() method.
        super(Fish, self).__init__(x, y, range, self.w_l, self.w_r, self.d_l,
                                   self.d_r, self.OB, self.LR)

        # When the fish is created this line of code changes the states object,
        # in enemy into FishNormalState.
        self.states = FishNormalState(self)
