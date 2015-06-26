import pygame
class Collider:

    left_right_collision = False
    previous_collision = ''
    one_time = False
    second_time = False
    level_state_manager = None
    main_menu = None

    is_collision = False
    player_behind = 0

    def __init__(self, player, map, enemy_list, level_state_manager, main_menu):
        self.player = player
        self.map = map
        self.enemy_list = enemy_list
        self.level_state_manager = level_state_manager
        self.main_menu = main_menu

    def update(self):
        self.player_collider()
        self.enemy_collider()
        self.player_enemy_collider()

    def player_collider(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.map, False)
        for block in blocks_hit_list:
            #if on exit sign , load next level
            if block.image_type == 114:
                self.level_state_manager.next_level(self.main_menu)

            #vertically
            if self.player.rect.bottom >= block.rect.top:
                if not self.player.rect.topleft[1] > block.rect.bottomright[1]:
                    pass
                
                if not block.rect.topleft[1] > self.player.rect.bottomright[1]:
                    self.player.collision_under = True

            #horizontally
            if self.player.rect.bottom >= block.rect.bottom:
                if not self.player.rect.topleft[0] > block.rect.bottomright[0] or block.rect.topleft[0] > self.player.rect.bottomright[0]:
                    if block.rect.left < self.player.rect.left and self.player.face_direction == 'Left':
                        self.player.canGoLeft = False
                        self.player.canGoRight = True

                    if block.rect.left < self.player.rect.left and self.player.face_direction == 'Right':
                        self.player.canGoLeft = True
                        self.player.canGoRight = True

                    if block.rect.right > self.player.rect.right and self.player.face_direction == 'Left':
                        self.player.canGoLeft = True
                        self.player.canGoRight = True

                    if block.rect.right > self.player.rect.right and self.player.face_direction == 'Right':
                        self.player.canGoLeft = True
                        self.player.canGoRight = False


        if not blocks_hit_list:
            self.player.collision_under = False


    def enemy_collider(self):
        for i in range(len(self.enemy_list)):
            blocks_hit_list = pygame.sprite.spritecollide(self.enemy_list[i], self.map, False)
            for block in blocks_hit_list:
                # Collision up
                if (self.enemy_list[i].rect.top <= block.rect.bottom and self.enemy_list[i].rect.top >= block.rect.top):
                    self.enemy_list[i].block_u = True
                else:
                    self.enemy_list[i].block_u = False

                # Collision under
                if (self.enemy_list[i].rect.bottom >= block.rect.top and self.enemy_list[i].rect.bottom <= block.rect.bottom):
                    self.enemy_list[i].block_d = True
                else:
                    self.enemy_list[i].block_d = False

                # Collision right
                if (self.enemy_list[i].rect.right >= block.rect.left and self.enemy_list[i].rect.right <= block.rect.right and
                    self.enemy_list[i].rect.bottom <= block.rect.bottom):
                    self.enemy_list[i].block_r = True
                else:
                    self.enemy_list[i].block_r = False

                #Collision left
                if (self.enemy_list[i].rect.left <= block.rect.right and self.enemy_list[i].rect.left >= block.rect.left and
                    self.enemy_list[i].rect.bottom <= block.rect.bottom):
                    self.enemy_list[i].block_l = True
                else:
                    self.enemy_list[i].block_l = False

            if not blocks_hit_list:
                self.enemy_list[i].block_u = False
                self.enemy_list[i].block_d = False
                self.enemy_list[i].block_l = False
                self.enemy_list[i].block_r = False

    def player_enemy_collider(self):

        for i in range(len(self.enemy_list)):

            # De enemy de player laten volgen wanneer hij in range is
            if self.enemy_list[i].rect.x - self.player.rect.x <= self.range and self.enemy_list[i].rect.x - self.player.rect.x >= -self.range:
                self.enemy_list[i].follow = True
            else:
                self.enemy_list[i].follow = False

            # Als de player in range is wordt er op deze manier door gegeven of de enemy naar
            # links of rechts moet lopen
            if self.enemy_list[i].follow:
                if self.enemy_list[i].rect.x > self.player.rect.x:
                    self.enemy_list[i].left_right = False
                else:
                    self.enemy_list[i].left_right = True

            blocks_hit_list = pygame.sprite.spritecollide(self.enemy_list[i], self.player_group, False)
            for block in blocks_hit_list:

                if self.player.ySpeed == 0 and not self.enemy_list[i].dead:
                    self.player.kill()
                elif self.player.ySpeed != 0 and not self.enemy_list[i].dead:
                    self.enemy_list[i].kill()
                    self.player.ySpeed = 5

    def objects_collider(self):
        for i in range(len(self.enemy_list)):
            if isinstance(self.enemy_list[i], Enemy.Tank.Tank):
                for j in range(self.enemy_list[i].get_len_bl()):

                    # als de enemy een tank is, voer de code uit om te kijken of de bullet de map raakt.
                    # Zoja dan explodeert hij
                    block_hit_list = pygame.sprite.spritecollide(self.enemy_list[i].get_bl()[j], self.map, False)
                    for hit in block_hit_list:
                        self.enemy_list[i].get_bl()[j].explode()

                    # Als de bullet de player raakt gaat de player dood en explodeert de bullet
                    block_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list[i].get_bl(), False)
                    for hit in block_hit_list:
                        self.player.kill()
                        self.enemy_list[i].get_bl()[j].explode()

                    if self.enemy_list[i].get_bl()[j].rect.x >= self.player.rect.x:
                        self.enemy_list[i].get_bl()[j].l_r = True
                    else:
                        self.enemy_list[i].get_bl()[j].l_r = False

                    if self.enemy_list[i].get_bl()[j].rect.y >= self.player.rect.y:
                        self.enemy_list[i].get_bl()[j].u_d = True
                    else:
                        self.enemy_list[i].get_bl()[j].u_d = False

            # Wanneer de enemy een slime is wordt er gekeken of de slime nieuwe snakes aangemaakt heeft.
            # Zoja, dan wordt die snake aan de enemy_list toegevoegd. Hierdoor werkt hij met de collider
            if isinstance(self.enemy_list[i], Enemy.Slime.Slime):
                if len(self.enemy_list[i].snake_list) > self.snake_hulp:
                    self.enemy_list.append(self.enemy_list[i].get_snake(self.snake_hulp))
                    self.snake_hulp += 1

            # Als de enemy een snake is wordt er gekeken of hij naar links of rechts moet lopen
            if isinstance(self.enemy_list[i], Enemy.Snake.Snake):
                if self.player.rect.x >= self.enemy_list[i].rect.x:
                    self.enemy_list[i].l_r = True
                else:
                    self.enemy_list[i].l_r = False