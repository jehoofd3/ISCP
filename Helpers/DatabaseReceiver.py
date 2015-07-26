import sqlite3
from PIL import Image
from cStringIO import StringIO
import pygame


class DatabaseReceiver(object):

    #Database File
    con = sqlite3.connect("../Data/Database/Escape_Database.db")
    cur = con.cursor()

    #Init hoeft niet perse?? (Artist?)

    @staticmethod
    def get_player_img(id):
        DatabaseReceiver.cur.execute("SELECT Image FROM player_images WHERE ID ='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    @staticmethod
    def get_enemy_img(enemy, id):
        DatabaseReceiver.cur.execute("SELECT Image FROM enemy_images WHERE Enemy ='" + enemy + "' AND ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    @staticmethod
    def get_map_img(id):
        DatabaseReceiver.cur.execute("SELECT Image FROM map_images WHERE ID ='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    @staticmethod
    def get_bullet_img(id):
        DatabaseReceiver.cur.execute("SELECT Image FROM bullet_images WHERE ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    @staticmethod
    def get_menu_img(id):
        DatabaseReceiver.cur.execute("SELECT Image FROM menu_images WHERE ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    @staticmethod
    def get_number_img(size, id):
        DatabaseReceiver.cur.execute("SELECT Image FROM number_images WHERE Size='" + size + "' AND ID='" + id + "'")

        return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])

    @staticmethod
    def get_level_data(data, level, id):
        DatabaseReceiver.cur.execute("SELECT Data FROM level_data WHERE Level='" + level + "' AND ID='" + id + "'")

        if data == "IMAGE":
            return DatabaseReceiver.convert_img(DatabaseReceiver.cur.fetchone()[0])
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

    @staticmethod
    def convert_img(bytecode):
        imgfile = StringIO(bytecode)
        img = Image.open(imgfile)

        mode = img.mode
        size = img.size
        data = img.tostring()

        return pygame.image.fromstring(data, size, mode).convert_alpha()
