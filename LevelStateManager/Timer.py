from Helpers.Artist import *
from Helpers.DatabaseReceiver import *
import sqlite3

class Timer:

    numbers = []
    numbers_small = []
    time = []
    best_time = []
    can_draw = []
    MILLISEC_PASSED_EVENT = pygame.USEREVENT + 1

    klok = DatabaseReceiver.get_number_img("Klok", "Klok")
    no_time_line = DatabaseReceiver.get_number_img("No_time", "No_time")

    timer_start_x = 820

    def __init__(self):
        self.time = [0, 0, 0, 0]
        self.can_draw = [False, False, False, True]
        for x in range(0, 10):
            self.numbers.append(DatabaseReceiver.get_number_img("Big", "hud_" + str(x)))

        for x in range(0, 10):
            self.numbers_small.append(DatabaseReceiver.get_number_img("Small", "hud_" + str(x)))

        pygame.time.set_timer(self.MILLISEC_PASSED_EVENT, 100)

    def update(self):
        for event in pygame.event.get(self.MILLISEC_PASSED_EVENT):
            self.time[3] += 1

        #zero number four
        if self.time[3] > 9:
            self.time[2] += 1
            self.time[3] = 0
            self.can_draw[2] = True

        #zero number three
        if self.time[2] > 9:
            self.time[1] += 1
            self.time[2] = 0
            self.can_draw[1] = True

        #zero number two
        if self.time[1] > 9:
            self.time[0] += 1
            self.time[1] = 0
            self.can_draw[0] = True

        #zero number one
        if self.time[0] > 9:
            self.reset_time()

        if self.time[0] >= 9 and self.time[1] >= 9 and self.time[2] >= 9 and self.time[3] >= 9:
            self.reset_time()

    def draw(self):
        self.draw_clock()
        self.draw_timer()
        self.draw_best_time()

    def draw_clock(self):
        Artist.draw_textures(self.klok, (770, 50))

    def draw_timer(self):
        x = self.timer_start_x
        for i in range(0, 4):
            if self.can_draw[i]:
                if i == 3:
                    x += 6
                    Artist.draw_textures(self.numbers_small[self.time[i]], (x, 75))
                    break

                Artist.draw_textures(self.numbers[self.time[i]], (x, 60))
            x += 30

    def reset_time(self):
        self.time = [0, 0, 0, 0]

    # Save the best time in the database
    def save_best_time(self, level):
        time_temp = self.time[0] * 100 + self.time[1] * 10 + self.time[2] + self.time[3] * 0.1
        best_time_temp = self.best_time[0] * 100 + self.best_time[1] * 10 + self.best_time[2] + self.best_time[3] * 0.1

        if time_temp < best_time_temp or best_time_temp == 0:
            DatabaseReceiver.save_timer(str(self.time[0]), str(self.time[1]),
                                        str(self.time[2]), str(self.time[3]), str(level))

    # Get the best time from database and put it in best_time array
    def load_best_time(self, level):
        self.best_time = DatabaseReceiver.load_timer(str(level))

    def draw_best_time(self):
        x = self.timer_start_x

        if self.best_time[0] == 0 and self.best_time[1] == 0 and self.best_time[2] == 0 and self.best_time[3] == 0:
            Artist.draw_textures(self.no_time_line, (x + 50, 700))

        for i in range(0, 4):
            if self.best_time[i] == 0:
                x += 30
                continue

            if i == 3:
                x += 6
                Artist.draw_textures(self.numbers_small[self.best_time[i]], (x, 715))
                break
            Artist.draw_textures(self.numbers[self.best_time[i]], (x, 700))
            x += 30

    def reset_best_time(self, level):
        DatabaseReceiver.reset_timer()
        self.load_best_time(level)
