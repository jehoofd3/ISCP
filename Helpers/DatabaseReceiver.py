import sqlite3
from PIL import Image
from cStringIO import StringIO
import pygame


class DatabaseReceiver(object):

    # The con variable opens a connection to the SQLite database file
    # Escape_Database.db.
    # The cur variable return a cursor for the connection so it is
    # possible to execute sqlite statements.

    con = sqlite3.connect("../Data/Database/Escape_Database.db")
    cur = con.cursor()

    # This method uses the cur variable to receive a bytecode from
    # the database.
    # It uses the id variable (String) to get the right
    # bytecode (image).
    # When the database returns the bytecode, the method calls another
    # method called convert_img.
    # This method convert the bytecode into an image and returns this
    # image (explained later in this class).
    # Then this method returns the image to its caller.

    @staticmethod
    def get_player_img(id):
        DatabaseReceiver.cur.execute\
            ("SELECT Image FROM player_images WHERE ID ='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    # This method uses the cur variable to receive a bytecode from
    # the database.
    # It uses the enemy and id variable (both String) to get the right
    # bytecode (image).
    # When the database returns the bytecode, the mehod calls another
    # method called convert_img.
    # This method convert the bytecode into an image and returns this
    # image (explained later in this class).
    # Then this method returns the image to its caller.

    @staticmethod
    def get_enemy_img(enemy, id):
        DatabaseReceiver.cur.execute\
            ("SELECT Image FROM enemy_images WHERE Enemy ='"
             + enemy + "' AND ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    # This method uses the cur variable to receive a bytecode from
    # the database.
    # It uses the id variable (String) to get the right
    # bytecode (image).
    # When the database returns the bytecode, the method calls another
    # method called convert_img.
    # This method convert the bytecode into an image and returns this
    # image (explained later in this class).
    # Then this method returns the image to its caller.

    @staticmethod
    def get_map_img(id):
        DatabaseReceiver.cur.execute("SELECT Image FROM map_images WHERE ID ='"
                                     + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    # This method uses the cur variable to receive a bytecode from
    # the database.
    # It uses the id variable (String) to get the right
    # bytecode (image).
    # When the database returns the bytecode, the method calls another
    # method called convert_img.
    # This method convert the bytecode into an image and returns this
    # image (explained later in this class).
    # Then this method returns the image to its caller.

    @staticmethod
    def get_bullet_img(id):
        DatabaseReceiver.cur.execute\
            ("SELECT Image FROM bullet_images WHERE ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    # This method uses the cur variable to receive a bytecode from
    # the database.
    # It uses the id variable (String) to get the right bytecode (image).
    # When the database returns the bytecode, the method calls another
    # method called convert_img.
    # This method convert the bytecode into an image and returns this
    # image (explained later in this class).
    # Then this method returns the image to its caller.

    @staticmethod
    def get_menu_img(id):
        DatabaseReceiver.cur.execute("SELECT Image FROM menu_images WHERE ID='"
                                     + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    # This method uses the cur variable to receive a bytecode from
    # the database.
    # It uses the size and id variable (both String) to get the right
    # bytecode (image).
    # When the database returns the bytecode, the method calls another
    # method called convert_img.
    # This method convert the bytecode into an image and returns this
    # image (explained later in this class).
    # Then this method returns the image to its caller.
    @staticmethod
    def get_number_img(size, id):
        DatabaseReceiver.cur.execute\
            ("SELECT Image FROM number_images WHERE Size='"
             + size + "' AND ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    # The database contains a row of al the level data, including
    # images and numbers.
    # There are two options, the caller asks a image or a list of
    # numbers to create the map.
    # When the caller ask for a image, the data variable is IMAGE, then
    # it uses the same technique as mentioned above.
    # When the caller asks for a list of integers to create the map,
    # the data variable is TXT.
    # The data in the database is stored in a StringIO called output,
    # all the numbers are stored as a String.
    # The output.getvalue() convert the bytecode to a String.
    # The contents.strip() removes al the spaces and the
    # contents.split() removes the leading and trailing.
    # The strip = contents.strip() and end_string = strip.split()
    # combines these two methods,
    # so there is only a string of clear numbers.
    # Then the for loop places these numbers in a list and returns
    # this list to its caller.

    @staticmethod
    def get_level_data(data, level, id):
        DatabaseReceiver.cur.execute\
            ("SELECT Data FROM level_data WHERE Level='"
             + level + "' AND ID='" + id + "'")

        if data == "IMAGE":
            return DatabaseReceiver.convert_img\
                (DatabaseReceiver.cur.fetchone()[0])
        else:
            output = StringIO(DatabaseReceiver.cur.fetchone()[0])

            contents = output.getvalue()

            contents.strip()
            contents.split()
            strip = contents.strip()
            end_string = strip.split()

            map_list = [None] * 720

            for i in range(0, 720):
                map_list[i] = int(end_string[i])
            return map_list

    # Save the time from the timer class in the database.
    # We have one table with five columns.
    # The column names are: hundreds , tens, ones, tenths and the level.
    # We use the level column for the id.
    @staticmethod
    def save_timer(hundreds, tens, ones, tenths, level):
        # Update the time in the database with the variables.
        DatabaseReceiver.cur.execute\
            ('UPDATE best_time SET hundreds ='
             + hundreds + ', tens =' + tens + ', ones =' + ones + ', tenths ='
             + tenths + ' WHERE Level =' + level)
        DatabaseReceiver.con.commit()

    # Load the time from the database.
    @staticmethod
    def load_timer(level):
        # We use the SELECT query to get the time from the database.
        DatabaseReceiver.cur.execute\
            ('SELECT Hundreds, Tens, Ones, Tenths FROM best_time WHERE Level ='
             + level)
        # Return the output from the database.
        return DatabaseReceiver.cur.fetchone()

    # Reset the time from the timer in the database.
    @staticmethod
    def reset_timer():
        # Use the UPDATE query to set every variable to zero.
        DatabaseReceiver.cur.execute\
            ('UPDATE best_time SET Hundreds = 0, Tens = 0, Ones = 0, '
             'Tenths = 0')

    # This method is used by the other methods in this class.
    # Its function is to convert the bytecode from the database
    # into an pygame.image.
    # The bytecode is stored in a StringIO object and transferred
    # into a image using,
    # the Python Image Library (PIL) module.
    # To convert the image into a pygame.image file we need
    # three variables.
    # data, this is the bytecode of the image.
    # size, this is the size of the image, because the image is
    # created by PIL it is possible to use the .size method.
    # mode, this is the mode of the image, its is RGBA witch
    # means Red Green Blue Alpha.
    # The pygame.image.fromstring needs these variables to
    # create a image.
    # The .convert_alpha() removes al the transparent pixels
    # in the image.

    @staticmethod
    def convert_img(bytecode):
        imgfile = StringIO(bytecode)
        img = Image.open(imgfile)

        mode = img.mode
        size = img.size
        data = img.tostring()
        return pygame.image.fromstring(data, size, mode).convert_alpha()
