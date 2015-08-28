from Enemy import *
from TankNormalState import *
from TankShootState import *
from Helpers.Artist import *
from Bullet.Bullet import *
from Helpers.Artist import *
from Player.Player import *
from Helpers.DatabaseReceiver import *


class Tank(Enemy):
    # These four variables are used to store the images.
    # w_l and w_r are lists the other two are objects.
    w_l, w_r, d_l, d_r = [], [], None, None

    def __init__(self, x, y, range):
        self.w_l = []
        self.w_r = []

        # This variables are images and it is used for the collision
        # with other objects.
        # This technique is hard to explain without images so how
        # exactly works is described in our report.
        self.OB = DatabaseReceiver.get_enemy_img("Tank", "Tank_OB")
        self.LR = DatabaseReceiver.get_enemy_img("Tank", "Tank_LR")

        # These methods are stored in the DatabaseReceiver class,
        # all the images are stored in the database.
        # These methods get them from the database and add them to the
        # image lists.
        self.w_l.append(DatabaseReceiver.get_enemy_img("Tank", "l_0"))
        self.w_l.append(DatabaseReceiver.get_enemy_img("Tank", "l_1"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Tank", "r_0"))
        self.w_r.append(DatabaseReceiver.get_enemy_img("Tank", "r_1"))
        self.d_l = DatabaseReceiver.get_enemy_img("Tank", "d_l")
        self.d_r = DatabaseReceiver.get_enemy_img("Tank", "d_r")

        # This game is object oriented and the class extends from Enemy
        # so its required
        # to call the super class by using the super() method.
        super(Tank, self).__init__(x, y, range, self.w_l, self.w_r,
                                   self.d_l, self.d_r, self.OB, self.LR)
        # When the tank is created this line of code changes the states
        # object in enemy into TankNormalState.
        self.states = TankNormalState(self)

    # Because of overloading this method is called in the levelstate's.
    # The tank needs to use it because it can shoot bullets.
    # These bullets needs to update every frame.
    def update(self):
        # This line of code calls the update function of the
        # super class.
        super(Tank, self).update()

        # This for loop calls the update function of the bullets in,
        # the bullet list.
        for b in self.bullet_list:
            b.update()

    # Because of overloading this method is called in the levelstate's.
    # The tank needs to use it because it can shoot bullets.
    # These bullets needs to draw every frame.
    def draw(self):
        # This line of code calls the update function of the super class
        super(Tank, self).draw()

        # This for loop calls the draw function of the bullets in,
        # the bullet list.
        for b in self.bullet_list:
            b.draw()

    # This method takes two integers (x, y) and one boolean
    # (left_right).
    # It adds an bullet to the bullet_list.
    # This makes a new Bullet object.
    def add_bullet(self, x, y, left_right):
        self.bullet_list.append(Bullet(x, y, left_right))

    # This method returns the bullet_list back to its caller.
    def get_bullet_list(self):
        return self.bullet_list
