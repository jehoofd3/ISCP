from Map.Tile import *
from Helpers.Artist import *
from Helpers.DatabaseReceiver import *

# This is a class that creates the map. It also give a type to certain images.
# Every level exists out of a tilegrid where every tile is a Sprite.
# We use 60 rows and 12 columns of tiles for every level.
#
# The tilegrid will create the map based of a txt.
# We made these txt with our editor made in java.
# More info in our report.

# Author: Richard Jongenburger


class TileGrid():
    # Make a pygame sprite group.
    # This group is a container for Sprites.
    map_group = pygame.sprite.Group()

    background_image = None

    # This is the number of rows and columns in the map.
    rows = 60
    columns = 12

    # Player's x coordinate.
    player_x = 0

    # Get the game surface from the Artist class.
    display = Artist.get_display()

    def __init__(self, level_list):
        # Empty the map group.
        # We do this so that the map_group
        # will empty when you create a new map.
        # Otherwise it just adds to the existing map group
        # and the sprites of the previous level are still in the container.
        # So it's used to ensure that only the tiles of one level is in the
        # container.
        self.map_group.empty()

        counter = 0
        # Loop through every row and column.
        for i in range(self.columns):
            for j in range(self.rows):
                # Makes sure that the image type
                # is back to empty at each iteration.
                image_type = ''

                # The level_list exist out of (60 rows x 12 columns) 720 items.
                # Each item exist of a number that
                # corresponds to the names of the images in the database.
                # If the number is one or zero, it means that there
                # isn't a tile with an image on that place.
                # Ex: 80.jpg is a image of lava.
                # Each iteration we get an item
                # of level_list and put it in image_number.
                image_number = level_list[counter]

                # Add one to counter after each iteration.
                counter += 1

                # These following statements
                # are giving some images an image type.
                #
                # This gives image number 80, 81, 82 the 'Lava' type.
                for x in range(80, 83):
                    if image_number == x:
                        image_type = 'Lava'

                for x in range(83, 86):
                    if image_number == x:
                        image_type = 'Water'

                for x in range(117, 135):
                    if x == 118 or x == 119:
                        continue
                    elif image_number == x:
                        image_type = 'Snow'

                for x in range(156, 172):
                    if image_number == x:
                        image_type = 'Ice'

                if image_number == 114:
                    image_type = 'Exit'

                # ImageNumber 1 or 0 means that there isn't a sprite
                # on that location in the tilegrid.
                # So we go to the next iteration.
                if image_number == -1 or image_number == 0:
                    pass
                else:
                    # Make a Tile with the specified x, y coordinate,
                    # the image and the type of the image.
                    # We do the j and i times 64, because our tiles exist of
                    # 64 x 64 pixels.
                    # After that we add it to the map_group container.
                    self.map_group.add(Tile(j * 64, i * 64, DatabaseReceiver.
                                            get_map_img(str(image_number)),
                                            image_type))

    def run(self):
        pass

    # Draw every sprite of the tilegrid on the surface.
    def draw(self):
        self.map_group.draw(Artist.get_display())

    # Method to change the x of every tile on the map with
    # the player's x speed.
    # So that the map moves along with the player.
    def shift_map(self, player_x_speed):
        # Change the player's x according to the players x_speed.
        self.player_x += player_x_speed

        # Loop through every tile in the map.
        for sprite in self.map_group:
            # Change the tiles their x with the player_x_speed.
            sprite.shift_x(player_x_speed)

    # Needed for the collider class.
    @staticmethod
    def get_group():
        return TileGrid.map_group

    # This method is used to set the player_x variable to
    # the player_spawn_x variable when a new level is created.
    def set_player_x(self, player_spawn_x):
        self.player_x = player_spawn_x
