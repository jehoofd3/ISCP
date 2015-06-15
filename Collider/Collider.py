import pygame
import Enemy


class Collider(object):

    def __init__(self, player, map, enemy_list):
        self.player = player
        self.map = map
        self.enemy_list = enemy_list
        self.range = 150

        # De player moet in een group gezet worden. Wanneer je een enemy killt, kill je ze allemaal.
        # Zo los je het probleem op
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player)

    def update(self):
        self.player_collider()
        self.enemy_collider()
        self.player_enemy_collider()
        self.bullet_collider()

    def player_collider(self):
        # Player killen wanneer hij met zijn onderkant (player.rect.bottom) de onderkant
        # van het scherm aanraakt 768 is de height van het scherm
        if self.player.rect.bottom > 768:
            self.player.kill()

        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.map, False)
        for block in blocks_hit_list:

            # Collision up
            if (self.player.rect.top <= block.rect.bottom and self.player.rect.top >= block.rect.top):
                self.player.block_u = True
            else:
                self.player.block_u = False

            # Collision under
            if (self.player.rect.bottom >= block.rect.top and self.player.rect.bottom <= block.rect.bottom):
                self.player.block_d = True

            else:
                self.player.block_d = False

            #Collision left
            if (self.player.rect.left <= block.rect.right and self.player.rect.left >= block.rect.left and
                self.player.rect.bottom <= block.rect.bottom):
                self.player.block_l = True
            else:
                self.player.block_l = False

            # Collision right
            if (self.player.rect.right >= block.rect.left and self.player.rect.right <= block.rect.right and
                self.player.rect.bottom <= block.rect.bottom):
                self.player.block_r = True
            else:
                self.player.block_r = False

        # Als de list leeg is, betekend het dat de player geen collision met Tile(s) heeft. Door alle variablen op False
        # te zetten blijft de Gravity actief en kan de player naar links / rechts bewegen en springen
        if not blocks_hit_list:
            self.player.block_u = False
            self.player.block_d = False
            self.player.block_l = False
            self.player.block_r = False

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
            if self.enemy_list[i].rect.x - self.player.rect.x <= self.range and \
                self.enemy_list[i].rect.x - self.player.rect.x >= -self.range:
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

    def bullet_collider(self):
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
                        self.player.dead = True
                        self.enemy_list[i].get_bl()[j].explode()

                    if self.enemy_list[i].get_bl()[j].rect.x >= self.player.rect.x:
                        self.enemy_list[i].get_bl()[j].l_r = True
                    else:
                        self.enemy_list[i].get_bl()[j].l_r = False

                    if self.enemy_list[i].get_bl()[j].rect.y >= self.player.rect.y:
                        self.enemy_list[i].get_bl()[j].u_d = True
                    else:
                        self.enemy_list[i].get_bl()[j].u_d = False
