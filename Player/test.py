'''

    def player_collider(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.map, False)
        for block in blocks_hit_list:
            print 'g'
            if self.player.rect.bottom >= block.rect.bottom:
                if self.player.rect.left <= block.rect.right or self.player.rect.right >= block.rect.left:
                    self.left_right_collision = True
                    if self.player.face_direction == 'Left' and not self.previous_collision == 'Right':
                        self.player.canGoLeft = False
                        self.player.canGoRight = True
                        self.previous_collision = 'Left'
                    if self.player.face_direction == 'Right' and not self.previous_collision == 'Left':
                        self.player.canGoRight = False
                        self.player.canGoLeft = True
                        self.previous_collision = 'Right'

            else:
                self.left_right_collision = False

            #als er geen collision is kan je naar links en rechts lopen
            if not self.left_right_collision:
                self.previous_collision = ''
                self.player.canGoLeft = True
                self.player.canGoRight = True

            #top
            if self.player.rect.bottom >= block.rect.bottom:
                pass

            #bottom
            if self.player.rect.top < block.rect.bottom:
                self.player.collision_under = True

'''
