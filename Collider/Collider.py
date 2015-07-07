import pygame
import Enemy
from Helpers.Artist import *

class Collider(object):

    level_state_manager = None
    main_menu = None
    snake_hulp = 0
    range = 200
    player_group = pygame.sprite.Group()

    is_collision = False
    player_behind = 0

    def __init__(self, player, map, enemy_list, level_state_manager, main_menu):
        self.player = player
        self.map = map
        self.enemy_list = enemy_list
        self.level_state_manager = level_state_manager
        self.main_menu = main_menu
        self.player_group.add(player)

    def update(self):
        self.player_collision_map_objects()
        self.player_collision_down()
        self.player_collision_up()
        self.player_collision_left()
        self.player_collision_right()

        self.enemy_collision_down()
        self.enemy_collision_up()
        self.enemy_collision_left()
        self.enemy_collision_right()

        self.player_enemy_collider()
        self.objects_collider()

        if self.player.rect.x <= 0:
            self.player.canGoLeft = False

        if self.player.rect.x >= Artist.get_screen_width() - 70:
            self.player.canGoRight = False

    # Collision between the player and all the images of the map.
    # This pygame method puts all of the map images where the player collides with in a list.
    # It needs a sprite as the first parameter, and it needs a sprite group as the second parameter.
    #
    def player_collision_map_objects(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.map, False)

        for block in blocks_hit_list:
            if block.image_type == 114:
                self.level_state_manager.next_level()
            #test
            if block.image_type == 80 or block.image_type == 81 or block.image_type == 82 or block.image_type == 83 or block.image_type == 84 or block.image_type == 85:
                self.player.kill()

    def player_collision_down(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player.player_under_image, self.map, False)

        if blocks_hit_list:
            self.player.collision_under = True
        else:
            self.player.collision_under = False

    def player_collision_up(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player.player_up_image, self.map, False)

        if blocks_hit_list:
            self.player.collision_up = True
        else:
            self.player.collision_up = False

    def player_collision_left(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player.player_left_image, self.map, False)

        if blocks_hit_list:
            self.player.canGoLeft = False
        else:
            self.player.canGoLeft = True

    def player_collision_right(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player.player_right_image, self.map, False)

        if blocks_hit_list:
            self.player.canGoRight = False
        else:
            self.player.canGoRight = True

    def enemy_collision_down(self):
        for e in self.enemy_list:
            blocks_hit_list = pygame.sprite.spritecollide(e.enemy_under_image, self.map, False)

            if blocks_hit_list:
                e.block_d = True
            else:
                e.block_d = False

    def enemy_collision_up(self):
        for e in self.enemy_list:
            blocks_hit_list = pygame.sprite.spritecollide(e.enemy_up_image, self.map, False)

            if blocks_hit_list:
                e.block_u = True
            else:
                e.block_u = False

    def enemy_collision_left(self):
        for e in self.enemy_list:
            blocks_hit_list = pygame.sprite.spritecollide(e.enemy_left_image, self.map, False)

            if blocks_hit_list:
                e.block_l = True
            else:
                e.block_l = False

    def enemy_collision_right(self):
        for e in self.enemy_list:
            blocks_hit_list = pygame.sprite.spritecollide(e.enemy_right_image, self.map, False)

            if blocks_hit_list:
                e.block_r = True
            else:
                e.block_r = False

    def player_enemy_collider(self):
        for e in self.enemy_list:
            # De enemy de player laten volgen wanneer hij in range is
            if e.rect.x - self.player.rect.x <= self.range and \
                e.rect.x - self.player.rect.x >= -self.range and \
                e.rect.y - self.player.rect.y <= self.range * 2 and \
                e.rect.y - self.player.rect.y >= -self.range * 2:
                e.follow = True
            else:
                e.follow = False

            # Als de player in range is wordt er op deze manier door gegeven of de enemy naar
            # links of rechts moet lopen
            if e.follow:
                if e.rect.x > self.player.rect.x:
                    e.left_right = False
                else:
                    e.left_right = True

            blocks_hit_list = pygame.sprite.spritecollide(e, self.player_group, False)
            for block in blocks_hit_list:
                if self.player.ySpeed == 0 and not e.dead:
                    self.player.kill()
                elif self.player.ySpeed != 0 and not e.dead:
                    e.kill()
                    self.player.ySpeed = 5

    def objects_collider(self):
        for e in self.enemy_list:
            if isinstance(e, Enemy.Tank.Tank):
                for b in e.get_bl():
                    if b.active:
                        # De kogel laten exploderen wanneer hij collision met de map heeft
                        map_hit = pygame.sprite.spritecollide(b, self.map, False)
                        if map_hit:
                            b.explode()

                        # De player killen en de kogel laten exploderen wanneer de kogel de player raakt
                        player_hit = pygame.sprite.spritecollide(self.player, e.get_bl(), False)
                        if player_hit:
                            if b.active:
                                self.player.kill()
                                b.explode()

                        if b.rect.x >= self.player.rect.x:
                            b.l_r = True
                        else:
                            b.l_r = False

                        if b.rect.y >= self.player.rect.y:
                            b.u_d = True
                        else:
                            b.u_d = False

            if isinstance(e, Enemy.Slime.Slime):
                if len(e.snake_list) > self.snake_hulp:
                    self.enemy_list.append(e.get_snake(self.snake_hulp))
                    self.snake_hulp += 1

            # Als de enemy een snake is wordt er gekeken of hij naar links of rechts moet lopen
            if isinstance(e, Enemy.Snake.Snake):
                if self.player.rect.x >= e.rect.x:
                    e.l_r = True
                else:
                    e.l_r = False
