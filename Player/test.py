'''

            if self.player.rect.bottom >= block.rect.top and self.player.rect.right >= block.rect.left:
                self.player.rect.bottom = block.rect.top
                print True

            if block.rect.left >= self.player.rect.right:
                print True

            if self.player.rect.top >= block.rect.bottom:
                self.player.rect.top = block.rect.bottom

            if self.player.rect.left >= block.rect.right:
                self.player.rect.left = block.rect.right

            if self.player.rect.right <= block.rect.left:
                self.player.rect.right = block.rect.left
'''
