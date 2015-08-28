class EnemyAnimation(object):

    # This constructor needs al the images of an enemy.
    # walk_l and walk_r are lists containing the images for
    # the walk animation.
    # The dead_l and dead_r are the images for the dead animations.
    def __init__(self, walk_l, walk_r, dead_l, dead_r):
        # These four variables are created to store the images in.
        self.walk_l = walk_l
        self.walk_r = walk_r
        self.dead_l = dead_l
        self.dead_r = dead_r

        # The texture variable is an image, when the update method
        # calculate an image, it is stored in texture and send back
        # to the enemy.
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
        # If there are two images in walk_l, the update function
        # changes the image after 30 frames (0.5 seconds).
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

    # This method needs the x_speed integer and the dead boolean.
    def update(self, x_speed, dead):
        # If the expired frames are equal to frame_cap.
        if self.frame_count == self.frame_cap:
            # Set the frame_count back to 0.
            self.frame_count = 0

        # If the enemy is moving in the right direction.
        if x_speed > 0:
            # Call the right_walk method.
            self.right_walk()
            # And set the left_right boolean False
            self.left_right = False
        else:
            # Call the left_walk method.
            self.left_walk()
            # And set the left_right boolean True.
            self.left_right = True

        # If the enemy is dead, call the dead method.
        if dead:
            self.dead()

        # Add 1 to the frame_count variable.
        self.frame_count += 1

        # This line of code returns the image back to the enemy.
        return self.texture

    def right_walk(self):
        # This for loop loops trough the walk_r list.
        for i in range(self.length_list):
            # If the current amount of frames divided by tex_switch
            # is equal to the number of image in walk_r.
            if self.frame_count / self.tex_switch == i:
                # Change texture to the image in walk_r
                self.texture = self.walk_r[i]

    def left_walk(self):
        # This for loop loops trough the walk_l list.
        for i in range(self.length_list):
            # If the current amount of frames divided by tex_switch
            # is equal to the number of image in walk_l.
            if self.frame_count / self.tex_switch == i:
                # Change texture to the image in walk_l.
                self.texture = self.walk_l[i]

    def dead(self):
        # If the left_right boolean is True.
        if self.left_right:
            # Change the texture to the dead_r texture.
            self.texture = self.dead_r
        # If left_right is False
        else:
            # Change the texture to the dead_l texture.
            self.texture = self.dead_l
