
class Camera:

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

    def update(self):
        # Code that it will only shift between the given values
        if not self.player.is_shifting:
            self.map.x_start_shift_map += self.player.xSpeed

        if self.shift_start <= self.map.x_start_shift_map <= self.shift_end:
            self.player.is_shifting = True
            self.map.shift_map(self.player.get_player_x_speed())

            for e in self.enemy_list:
                e.move_with_map(self.player.get_player_x_speed())

        else:
            self.player.is_shifting = False
        # end shift map
