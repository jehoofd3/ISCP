import pygame
import Enemy
from Helpers.Artist import *

# Author: Richard Jongenburger
#         Jeroen van Ottelen

# The collider exist of 4 images placed around the player.
# Those images have a shape of a bar.
# We let those 4 images move along with the player.
# (We do all of this in the player class)
# In this class we check with each image to which tiles it has
# collision with.
# And we restrict the player's movement accordingly.


class Collider(object):

    # Make a reference to the LevelStateManager.
    # This is used to open the next level when the player collides
    # with the exit sign.
    level_state_manager = None

    # This variable is used to check is the player and enemy
    # are in range to switch the enemy state.
    range = 250

    # The collider needs an player group object.
    player_group = None
    player_collision_img = []

    # Temporary variable to hold boolean values for the collision.
    # The boolean values represent the following:
    # Under collision, Up collision, Left collision, Right collision.
    is_collision_temp = [False, False, False, False]

    # The constructor needs the player, map, enemy_list and
    # the level_state_manager.
    def __init__(self, player, map, enemy_list, level_state_manager):
        # Make a container to hold the player sprite.
        self.player_group = pygame.sprite.Group()

        # Hold the 4 collider images.
        self.player_collision_img = []

        # Add the objects from the constructor to the objects
        # from the class
        self.player = player
        self.map = map
        self.enemy_list = enemy_list
        self.level_state_manager = level_state_manager

        # Add the player to the player_group container.
        self.player_group.add(player)

        # Adding the four collision images to the player_collision
        # img array.
        self.player_collision_img.append(self.player.player_under_image)
        self.player_collision_img.append(self.player.player_up_image)
        self.player_collision_img.append(self.player.player_left_image)
        self.player_collision_img.append(self.player.player_right_image)

        # Update the enemy collider.
        self.update_enemy_collider()

    def update(self):
        # Method to check if there is collision between
        # the player and the tiles.
        self.player_collision_map_objects()

        # Check if there is collision with the player_under_image
        # and the tiles.
        self.player_collision_under_map_objects()

        # Method to set the collision boolean value.
        # (collision_up, collision_down, can_go_left and can_go_right)
        self.player_collision()

        # Call the method used to calculate the enemy collision.
        self.enemy_collision_map_objects()
        self.enemy_collision()

        # Call the method used to calculate the player collision.
        self.player_enemy_collider()

        # Call the method used to calculate the bullet collision.
        self.objects_collider()

        # Make sure that the player can't go
        # to the left when the player's x coordinate is 0.
        # So the player can't go out of the map.
        if self.player.rect.x <= 0:
            self.player.can_go_left = False

        # Make sure that the player can't go to the right
        # when the player's x coordinate is bigger then the screen width
        # minus the player's width (64).
        if self.player.rect.x >= Artist.get_screen_width() - 64:
            self.player.can_go_right = False

    # Collision between the player and all the tiles of the map.
    def player_collision_map_objects(self):
        # This pygame methods first checks
        # which tiles with the player collides.
        # Then he returns a list of tiles that collides with the player.
        # The first arguments needs a sprite, the second argument needs
        # a sprite group. The third argument makes sure
        # that the tiles it
        # collides with, won't be removed from the map list.
        blocks_hit_list = pygame.sprite.spritecollide(
            self.player, self.map, False)

        # Loop through every tile object that collides with the player.
        for block in blocks_hit_list:
            # Open the next level, when the tile is from the Exit type.
            if block.image_type == 'Exit':
                self.level_state_manager.next_level()

            # Kill the player when the tiles are from the water
            # or lava type.
            if block.image_type == 'Water' or block.image_type == 'Lava':
                    self.player.kill()

    # Collision between the collision under
    # image under the player and all the tiles of the map.
    def player_collision_under_map_objects(self):
        # This pygame methods first checks which tiles
        # with that player under image collides.
        # Then he returns a list of tiles that collides with the player.
        # The first arguments needs a sprite, the second argument
        # needs a sprite group.
        # The third argument makes sure that the tiles it
        # collides with, won't be removed from the map list.
        blocks_hit_list = pygame.sprite.spritecollide(
            self.player.player_under_image, self.map, False)

        # Loop through every tile object that
        # collides with the player_under_image.
        for block in blocks_hit_list:
            # Set player_on_snow to true
            # when there is collision with an snow image.
            if block.image_type == 'Snow':
                self.player.player_on_snow = True
            # Set it to false when there isn't collision between them.
            else:
                self.player.player_on_snow = False

            # Set player_on_ice to true
            # when there is collision with the an ice image.
            if block.image_type == 'Ice':
                self.player.player_on_ice = True
            # Set it to false when there isn't collision between them.
            else:
                self.player.player_on_ice = False

        # If the player is on snow and the player is facing right.
        if self.player.player_on_snow \
                and self.player.face_direction == 'Right':
            # Set the player speed on 2.
            self.player.set_sliding(2)
        elif self.player.player_on_snow:
            # If the player is on snow and
            # facing left, set the player speed on -2.
            self.player.set_sliding(-2)

        # If the player is on ice and the player is facing right.
        if self.player.player_on_ice and self.player.face_direction == 'Right':
            # Set the player speed on 8.
            self.player.set_sliding(8)
        elif self.player.player_on_ice:
            # If the player is on ice and
            # facing right, set the player speed on -8.
            self.player.set_sliding(-8)

        # If the player is not on snow or ice, set the
        # player speed on 4.
        # 4 is the normal speed.
        if not self.player.player_on_ice and not self.player.player_on_snow:
            self.player.set_sliding(4)

    def player_collision(self):
        # Loop through every image in player_collision_img array.
        for i in range(len(self.player_collision_img)):
            # This pygame methods first checks which tiles collides with
            # each image.
            # Then he returns a list of tiles that collides
            # with the image.
            # The first arguments needs a sprite, the second
            # argument needs a
            # sprite group. The third argument makes sure
            # that the tiles it
            # collides with, won't be removed from the map list.
            blocks_hit_list = pygame.sprite.spritecollide(
                self.player_collision_img[i], self.map, False)

            # If the list isn't empty, set the boolean
            # to true. So we know there is collision with that image.
            if blocks_hit_list:
                self.is_collision_temp[i] = True
            # If the list is empty, set it to false.
            # So we know there isn't collision with that image.
            else:
                self.is_collision_temp[i] = False

        # Set the boolean values that's are calculated in the for loop.
        self.player.collision_under = self.is_collision_temp[0]
        self.player.collision_up = self.is_collision_temp[1]

        # We need the opposite of the boolean values so we use the
        # not keyword.
        self.player.can_go_left = not self.is_collision_temp[2]
        self.player.can_go_right = not self.is_collision_temp[3]

    # This method checks if the enemy is colliding with an,
    # Water or lava tile.
    def enemy_collision_map_objects(self):
        # This loop loops trough the enemy_list.
        # This list contains al the enemies.
        for enemy in self.enemy_list:
            # The isinstance checks if the instance (enemy) is
            # not a fish.
            if not isinstance(enemy, Enemy.Fish.Fish):
                # The pygame spritecolide checks if the enemy is
                # colliding,
                # with the map.
                blocks_hit_list = pygame.sprite.spritecollide(enemy, self.map,
                                                              False)
                # The for loop loops trough the map objects (Tiles)
                # where the the enemy is colliding with.
                for block in blocks_hit_list:
                    # If this block is a water or lava tile.
                    if block.image_type == 'Water' or \
                                    block.image_type == 'Lava':
                            # Kill the enemy
                            enemy.kill()

    # This method checks if the enemy is colliding with the map.
    # It lets the enemy stand still on the map.
    def enemy_collision(self):
        # This loop loops trough the enemy_list.
        # This list contains al the enemies.
        for i in range(len(self.enemy_list)):
            # Al the enemies has four images that checks the collision.
            # The second for loop loops trough this images.
            for j in range(4):
                # The pygame spritecollide checks if this image is
                # colliding with an map object (Tile).
                blocks_hit_list = pygame.sprite.spritecollide\
                    (self.enemy_collision_img[i][j], self.map, False)

                # If the collision image is colliding
                # set an hulp variable True.
                if blocks_hit_list:
                    self.enemy_hulp[i][j] = True

                # If it is not colliding, set the hulp varible False.
                else:
                    self.enemy_hulp[i][j] = False

                # When the second for loop is finished.
                # Change al collision variables in enemy according
                # to the hulp variables
                self.enemy_list[i].block_d = self.enemy_hulp[i][0]
                self.enemy_list[i].block_u = self.enemy_hulp[i][1]
                self.enemy_list[i].block_l = self.enemy_hulp[i][2]
                self.enemy_list[i].block_r = self.enemy_hulp[i][3]

    # This method check the collision between the player en enemy.
    def player_enemy_collider(self):
        # This loop loops trough the enemy_list.
        # This list contains al the enemies.
        for e in self.enemy_list:
            # If the player is in range (250 pixels) of the enemy.
            # Change the follow boolean in enemy to True.
            # This makes it switch to its FollowState
            if e.rect.x - self.player.rect.x <= self.range and \
                e.rect.x - self.player.rect.x >= -self.range and \
                e.rect.y - self.player.rect.y <= self.range * 2 and \
                e.rect.y - self.player.rect.y >= -self.range * 2:
                e.follow = True

            # If the enemy is in range and the distance between the,
            # player and enemy is 450 pixels (range * 1.8).
            # Change the follow boolean in enemy to False.
            # This makes the enemy switch to tis NotmalState.
            elif e.rect.x - self.player.rect.x >= self.range * 1.8 or \
                e.rect.x - self.player.rect.x <= -self.range * 1.8 and \
                            e.follow:
                e.follow = False

            # Als de player in range is wordt er op deze manier door
            # gegeven of de enemy naar links of rechts moet lopen
            # If the enemy is in his FollowState.
            # (if the follow boolean is Treu).
            if e.follow:
                # If the x position of the enemy is greater than the
                # x position of the player.
                if e.rect.x > self.player.rect.x:
                    # Change the left_right boolean to False.
                    # This makes the enemy move to the left side.
                    e.left_right = False
                else:
                    # Else change the left_right boolean to True.
                    # This makes the enemy move to the right side.
                    e.left_right = True

            # This method checks if the under image of the player is
            # colliding with an enemy.
            # The under image is the underside of the player.
            # The if statement checks if the player and enemy are alive
            # (not e.dead and not self.player.dead).
            # And it checks if the y_speed of the player is not 0.
            if pygame.sprite.collide_rect(e, self.player.player_under_image):
                if not e.dead and not self.player.dead and \
                                self.player.y_speed != 0:
                    # Kill the enemy and let the player jump a
                    # little bit.
                    e.kill()
                    self.player.y_speed = 5

            # This variable checks if the player is colliding with the
            # enemy.
            blocks_hit_list = pygame.sprite.spritecollide \
                (e, self.player_group, False)
            for block in blocks_hit_list:
                # If the enemy and player are not dead.
                # Kill the player.
                if not e.dead and not self.player.dead:
                    self.player.kill()

    # This method checks the collision of the bullets.
    # And add new snakes to the enemy_list.
    def objects_collider(self):
        # This loop loops trough the enemy_list.
        # This list contains al the enemies.
        for e in self.enemy_list:
            # The isinstance checks if the enemy is an Tank.
            if isinstance(e, Enemy.Tank.Tank):
                # This loop loops trough the bullet_list of the Tank.
                for b in e.get_bullet_list():
                    # If the bullet is active.
                    if b.active:
                        # The sprite.spritecollide checks if the bullet,
                        # is colliding with the map.
                        map_hit = pygame.sprite.spritecollide\
                            (b, self.map, False)

                        # If it is colliding.
                        if map_hit:
                            # Explode the bullet.
                            b.explode()

                        # The sprite.spritecollide checks if the
                        # bullet and player are colliding.
                        player_hit = pygame.sprite.spritecollide\
                            (b, self.player_group, False)
                        # If they are colliding.
                        if player_hit:
                            # And if the bullet is active.
                            if b.active:
                                # Kill the player
                                self.player.kill()
                                # And explode the bullet.
                                b.explode()

            # If the enemy is an Slime
            if isinstance(e, Enemy.Slime.Slime):
                # This if state method checks if there is a new snake
                # in the snake_list.
                # The snake_hulp in Slime is used to check this.
                if len(e.snake_list) > e.snake_hulp:
                    # If the length of the list is greater than the
                    # snake_hulp variable.
                    # Add an snake to the snake_list (in Slime).
                    # The snake_hulp intiger is used to set the snake
                    # in the end of the list.
                    self.enemy_list.append(e.get_snake(e.snake_hulp))
                    # Add one to the snake_hulp integer in Slime.
                    e.snake_hulp += 1
                    # Call the update_enemy_collider method.
                    # This method adds the new Snake to the enemy_list.
                    # So it is possible to calculate the collision.
                    self.update_enemy_collider()

            # If the enemy is a Snake.
            if isinstance(e, Enemy.Snake.Snake):
                # If the x position of the Snake is greater than the the
                # x position of the player.
                if self.player.rect.x >= e.rect.x:
                    # Change the l_r boolean to True.
                    # This makes the Snake move to the left side.
                    e.l_r = True
                else:
                    # Change the l_r boolean to False.
                    # This makes the Snake move to the left side.
                    e.l_r = False

    # This method updates the enemy_list.
    def update_enemy_collider(self):
        # Create an multidimensional array.
        # It has four positions for the images used to calculate
        # The collidion.
        # And the length of the enemy_list, used to store the enemies.
        self.enemy_collision_img = [[[] for i in range(4)]
                                    for i in range(len(self.enemy_list))]

        # Set the images used to calculate the collision in the,
        # multidimensional.
        for i in range(len(self.enemy_list)):
            self.enemy_collision_img[i][0] = \
                self.enemy_list[i].enemy_under_image
            self.enemy_collision_img[i][1] = \
                self.enemy_list[i].enemy_up_image
            self.enemy_collision_img[i][2] = \
                self.enemy_list[i].enemy_left_image
            self.enemy_collision_img[i][3] = \
                self.enemy_list[i].enemy_right_image

        # Create a new multidimensional used to temporary store the
        # images used to calculate the collision.
        # This array is used in the enemy_collision method.
        self.enemy_hulp = [[[] for i in range(4)]
                           for i in range(len(self.enemy_list))]
