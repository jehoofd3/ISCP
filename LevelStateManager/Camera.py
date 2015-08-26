
class Camera(object):

    shift_start = 0
    shift_end = 0
    player = None
    map = None
    enemy_list = []

    def __init__(self, shift_start, shift_end, map, player, enemy_list):
        self.shift_start = shift_start
        self.shift_end = shift_end
        self.map = map
        self.player = player
        self.enemy_list = enemy_list

    def update_camera(self, player_x_speed):
        # Code that it will only shift between the given values
        if not self.player.is_shifting:
            self.map.x_start_shift_map += player_x_speed

        if self.shift_start <= self.map.x_start_shift_map <= self.shift_end:
            self.player.is_shifting = True
            self.map.shift_map(player_x_speed)

            for e in self.enemy_list:
                e.move_with_map(player_x_speed)

        else:
            self.player.is_shifting = False
            for e in self.enemy_list:
                e.move_with_map(0)
        # end shift map
