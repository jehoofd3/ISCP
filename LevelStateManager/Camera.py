
# Author: Richard Jongenburger

# Camera:
# It looks in the game like there is a camera that follows the player.
# But actually we are moving every tile and every
# enemy with the player's x speed.
# So the player is actually standing still.
#
# Only before the shift_start x coordinate
# and after the shift_x coordinate is the player moving.
# More info in the report.


class Camera:

    player = None
    map = None

    enemy_list = []

    # The X value on which the player needs to be
    # when starting to shift the map and stop shifting the map.
    shift_start = 0
    shift_end = 0

    # The constructor needs the shift_start, shift_end, map, player
    # and an enemy_list filled with enemy objects.
    def __init__(self, shift_start, shift_end, map, player, enemy_list):
        self.shift_start = shift_start
        self.shift_end = shift_end
        self.map = map
        self.player = player
        self.enemy_list = enemy_list

    def update_camera(self, player_x_speed):
        # Set the player's x coordinate in the map class
        # when the player isn't shifting.
        # (So set it when the player is before shift_start or after shift_end)
        if not self.player.is_shifting:
            self.map.player_x += player_x_speed

        # Test whether the player's x is between shift_start, shift_end.
        if self.shift_start < self.map.player_x < self.shift_end:
            self.player.is_shifting = True

            # Move all the tiles with the players x speed.
            self.map.shift_map(player_x_speed)

            # Move all the enemies with the player's x speed.
            for e in self.enemy_list:
                e.move_with_map(player_x_speed)

        # Don't move the map or the enemies when the
        # player's x is between shift_start and shift_end.
        else:
            self.player.is_shifting = False
            for e in self.enemy_list:
                e.move_with_map(0)
