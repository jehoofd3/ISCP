import pygame


class PlayerAnimation:

    # This constructor only needs the player.
    def __init__(self, player):
        # Because there is only one player, it is possible
        # to get al the images with the player object.
        self.player = player
        self.walk_l = self.player.walk_l
        self.walk_r = self.player.walk_r
        self.dead_l = self.player.dead_l
        self.dead_r = self.player.dead_r
        self.jump_l = self.player.jump_l
        self.jump_r = self.player.jump_r
        self.stand_l = self.player.stand_l
        self.stand_r = self.player.stand_r

        # The texture variable is an image, when the update method
        # calculate an image, it is stored in texture and send back
        # to the player.
        # This variable needs an default image, or else there will
        # be an error on the first frame
        # (because it sends an 'empty' image)
        self.texture = self.walk_l[0]

        # The frame_cap variable is an integer used to calculate
        # the image.
        # It define the maximal amount of frames that are calculated
        # every second.
        # We cap the max frames in the Boot class (clock.tick(60)).
        self.frame_cap = 60

        # This variable tells the update function after how many frames
        # he needs to change the image.
        # In modern game engines its used to show all the images in
        # 1 second (60 frames).
        # So the tex_switch divide the frame_cap by the length of
        # the list of images.
        # If there are eleven images in walk_l, the update function
        # changes the image after 5 frames (0.05 seconds).
        self.tex_switch = self.frame_cap / len(self.walk_l)

        # This variable counts the amount of frames.
        self.frame_count = 0

        # The left_right boolean checks the moving direction
        # of the enemy.
        # It is used to send the dead image.
        self.left_right = None

        # This integer is the length of the image list.
        # It is used by the loops.
        self.length_list = len(self.walk_l)

    # This method is used by the player and returns an image.
    def update(self):
        # If the expired frames are equal to frame_cap.
        if self.frame_count >= self.frame_cap:
            # Set the frame_count back to 0.
            self.frame_count = 0

        # If the player is moving in the right direction.
        # The player moves to the right if his x_speed
        # is greater than zero.
        if self.player.x_speed > 0:
            # Call the right_walk method.
            self.right_walk()
            # And set the left_right boolean False
            self.left_right = True
        # If the player is moving in the left direction.
        # The player moves to the left if his x_speed
        # is smaller than zero.
        elif self.player.x_speed < 0:
            # Call the left_walk method.
            self.left_walk()
            # And set the left_right boolean True.
            self.left_right = False

        # If the player stands still and left_right is True.
        # The player stands still if his x_speed is zero.
        elif self.player.x_speed == 0 and self.left_right:
            # Call the right_stand method.
            self.right_stand()

        # If the player stands still and left_right is False.
        # The player stands still if his x_speed is zero.
        elif self.player.x_speed == 0 and not self.left_right:
            # Call the left_stand method.
            self.left_stand()

        # If the player is moving in the air and left_right is True.
        # The player moves in the air if his y_speed is
        # not equal to zero.
        if self.player.y_speed != 0 and self.left_right:
            # Call the right_jump method.
            self.right_jump()

        # If the player is moving in the air and left_right is False.
        # The player moves in the air if his y_speed is not
        # equal to zero.
        elif self.player.y_speed != 0 and not self.left_right:
            # Call the left_jump method.
            self.left_jump()

        # If the player is dead.
        # The player is dead if the boolean dead in player is True.
        if self.player.dead:
            # Call the dead method.
            self.dead()

        # Add 1 to the frame_count variable.
        self.frame_count += 1

        # This line of code returns the image back to the player.
        return self.texture

    def right_walk(self):
        # This for loop loops trough the walk_r list.
        for i in range(self.length_list):
            # If the current amount of frames divided by tex_switch
            # is equal to the number of image in walk_r.
            if self.frame_count / self.tex_switch == i:
                # Change texture to the image in walk_r.
                self.texture = self.walk_r[i]

    def left_walk(self):
        # This for loop loops trough the walk_l list.
        for i in range(self.length_list):
            # If the current amount of frames divided by tex_switch
            # is equal to the number of image in walk_l.
            if self.frame_count / self.tex_switch == i:
                # Change texture to the image in walk_l
                self.texture = self.walk_l[i]

    # This method changes the texture to the stand_l image.
    def left_stand(self):
        self.texture = self.stand_l

    # This method changes the texture to the stand_r image.
    def right_stand(self):
        self.texture = self.stand_r

    # This method changes the texture to the jump_l image.
    def left_jump(self):
        self.texture = self.jump_l

    # This method changes the texture to the jump_r image.
    def right_jump(self):
        self.texture = self.jump_r

    def dead(self):
        # If the boolean left_right is True.
        if self.left_right:
            # Change the texture to the dead_r image.
            self.texture = self.dead_r
        # If the left_right boolean is False.
        else:
            # Change the texture to the dead_l image.
            self.texture = self.dead_l
