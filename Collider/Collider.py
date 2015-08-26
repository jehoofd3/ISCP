import pygame
import Enemy
from Helpers.Artist import *

# Author: Richard Jongenburger
#         Jeroen van Ottelen

# The collider exist of 4 images placed around the player.
# Those images have a shape of a bar.
# We let those 4 images move along with the player.
# (We do all of this in the player class)
# In this class we check with each image to which tiles it has collision.
# And restrict the player's movement accordingly.

class Collider(object):

    level_state_manager = None
    main_menu = None
    range = 250
    player_group = pygame.sprite.Group()
    player_collision_img = []

    # Temporary variable to hold boolean values for the collision.
    #
    # The boolean values represent the following:
    # Under collision, Up collision, Left collision, Right collision.
    is_collision_temp = [False, False, False, False]

    def __init__(self, player, map, enemy_list, level_state_manager):
        self.player_group = pygame.sprite.Group()
        self.player_collision_img = []

        self.player = player
        self.map = map
        self.enemy_list = enemy_list
        self.level_state_manager = level_state_manager
        self.player_group.add(player)

        # Adding the four collision images to a list.
        self.player_collision_img.append(self.player.player_under_image)
        self.player_collision_img.append(self.player.player_up_image)
        self.player_collision_img.append(self.player.player_left_image)
        self.player_collision_img.append(self.player.player_right_image)
        self.player_hulp = [None, None, None, None]

        self.update_enemy_collider()

    def update(self):
        # Call all the necessary methods of this class.
        self.player_collision_map_objects()
        self.player_collision_under_map_objects()
        self.player_collision()

        self.enemy_collision_map_objects()
        self.enemy_collision()

        self.player_enemy_collider()
        self.objects_collider()

        # Make sure that the player can't go
        # to the left when the player's x coordinate is 0.
        # So the player can't go out of the map.
        if self.player.rect.x <= 0:
            self.player.canGoLeft = False

        # Make sure that the player can't go to the right.
        # when the player's x coordinate is bigger then the screen width.
        if self.player.rect.x >= Artist.get_screen_width() - 64:
            self.player.canGoRight = False

    # Collision between the player and all the tiles of the map.
    def player_collision_map_objects(self):
        # This pygame methods first checks
        # which tiles with the player collides.
        # Then he returns a list of tiles that collides with the player.
        blocks_hit_list = pygame.sprite.spritecollide\
            (self.player, self.map, False)

        # Loop through every tile object that collides with the player.
        for block in blocks_hit_list:
            # Open the next level, when the tile is from the Exit type.
            if block.image_type == 'Exit':
                self.level_state_manager.next_level()

            # Kill the player when the tiles are from the water or lava type.
            if block.image_type == 'Water' or block.image_type == 'Lava':
                    self.player.kill()

    # Collision between the collision under
    # image under the player and all the tiles of the map.
    def player_collision_under_map_objects(self):
        # This pygame methods first checks which tiles
        # with that player under image collides.
        # Then he returns a list of tiles that collides with the player.
        blocks_hit_list = pygame.sprite.spritecollide\
            (self.player.player_under_image, self.map, False)

        # Loop through every tile object that
        # collides with the player under image.
        for block in blocks_hit_list:
            # Set player_on_snow to true
            # when there is collision with the an ice image.
            if block.image_type == 'Snow':
                self.player.player_on_snow = True
            else:
                self.player.player_on_snow = False

            # Set player_on_ice to true
            # when there is collision with the an ice image.
            if block.image_type == 'Ice':
                self.player.player_on_ice = True
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

        # If the player is not on snow or ice, set the player speed on 4.
        # 4 is normal speed.
        if not self.player.player_on_ice and not self.player.player_on_snow:
            self.player.set_sliding(4)

    def player_collision(self):
        # Loop through every image in player_collision_img.
        for i in range(len(self.player_collision_img)):
            # This pygame methods first checks
            # which tiles collides with each image.
            # Then he returns a list of tiles that collides with the image.
            blocks_hit_list = pygame.sprite.spritecollide\
                (self.player_collision_img[i], self.map, False)

            # If the list isn't empty, set the boolean
            # to true. So we know there is collision with that image.
            if blocks_hit_list:
                self.is_collision_temp[i] = True
            # If the list is empty, set it to false.
            # So we know there isn't collision with that image.
            else:
                self.is_collision_temp[i] = False

        # Set the boolean values.
        self.player.collision_under = self.is_collision_temp[0]
        self.player.collision_up = self.is_collision_temp[1]
        self.player.canGoLeft = self.is_collision_temp[2]
        self.player.canGoRight = self.is_collision_temp[3]

    def enemy_collision_map_objects(self):
        for enemy in self.enemy_list:
            if not isinstance(enemy, Enemy.Fish.Fish):
                blocks_hit_list = pygame.sprite.spritecollide(enemy, self.map, False)
                for block in blocks_hit_list:
                    if block.image_type == 'Water' or block.image_type == 'Lava':
                            enemy.kill()

    def enemy_collision(self):
        for i in range(len(self.enemy_list)):
            for j in range(4):
                blocks_hit_list = pygame.sprite.spritecollide(self.enemy_collision_img[i][j], self.map, False)
                if blocks_hit_list:
                    self.enemy_hulp[i][j] = True
                else:
                    self.enemy_hulp[i][j] = False

                self.enemy_list[i].block_d = self.enemy_hulp[i][0]
                self.enemy_list[i].block_u = self.enemy_hulp[i][1]
                self.enemy_list[i].block_l = self.enemy_hulp[i][2]
                self.enemy_list[i].block_r = self.enemy_hulp[i][3]

    def player_enemy_collider(self):
        for e in self.enemy_list:
            # De enemy de player laten volgen wanneer hij in range is
            if e.rect.x - self.player.rect.x <= self.range and \
                e.rect.x - self.player.rect.x >= -self.range and \
                e.rect.y - self.player.rect.y <= self.range * 2 and \
                e.rect.y - self.player.rect.y >= -self.range * 2:
                e.follow = True
            elif e.rect.x - self.player.rect.x >= self.range * 1.8 or \
                e.rect.x - self.player.rect.x <= -self.range * 1.8 and e.follow:
                e.follow = False

            # Als de player in range is wordt er op deze manier door gegeven of de enemy naar
            # links of rechts moet lopen
            if e.follow:
                if e.rect.x > self.player.rect.x:
                    e.left_right = False
                else:
                    e.left_right = True

            if pygame.sprite.collide_rect(e, self.player.player_under_image):
                if not e.dead and not self.player.dead and self.player.y_speed != 0:
                    e.kill()
                    self.player.y_speed = 5

            blocks_hit_list = pygame.sprite.spritecollide(e, self.player_group, False)
            for block in blocks_hit_list:
                if not e.dead and not self.player.dead:
                    self.player.kill()

    def objects_collider(self):
        for e in self.enemy_list:
            if isinstance(e, Enemy.Tank.Tank):
                for b in e.get_bullet_list():
                    if b.active:
                        # De kogel laten exploderen wanneer hij collision met de map heeft
                        map_hit = pygame.sprite.spritecollide(b, self.map, False)
                        if map_hit:
                            b.explode()

                        # De player killen en de kogel laten exploderen wanneer de kogel de player raakt
                        player_hit = pygame.sprite.spritecollide(b, self.player_group, False)
                        if player_hit:
                            if b.active:
                                self.player.kill()
                                b.explode()

            if isinstance(e, Enemy.Slime.Slime):
                if len(e.snake_list) > e.snake_hulp:
                    self.enemy_list.append(e.get_snake(e.snake_hulp))
                    e.snake_hulp += 1
                    self.update_enemy_collider()

            # Als de enemy een snake is wordt er gekeken of hij naar links of rechts moet lopen
            if isinstance(e, Enemy.Snake.Snake):
                if self.player.rect.x >= e.rect.x:
                    e.l_r = True
                else:
                    e.l_r = False

    def update_enemy_collider(self):
        self.enemy_collision_img = [[[] for i in range(4)] for i in range(len(self.enemy_list))]

        for i in range(len(self.enemy_list)):
            self.enemy_collision_img[i][0] = self.enemy_list[i].enemy_under_image
            self.enemy_collision_img[i][1] = self.enemy_list[i].enemy_up_image
            self.enemy_collision_img[i][2] = self.enemy_list[i].enemy_left_image
            self.enemy_collision_img[i][3] = self.enemy_list[i].enemy_right_image

        self.enemy_hulp = [[[] for i in range(4)] for i in range(len(self.enemy_list))]
