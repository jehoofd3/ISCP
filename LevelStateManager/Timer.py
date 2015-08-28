from Helpers.Artist import *
from Helpers.DatabaseReceiver import *
import sqlite3

# Author: Richard Jongenburger


class Timer:

    # Array with images of the numbers.
    numbers = []

    # Array with the images of the small numbers.
    numbers_small = []

    # Array that represents the time.
    time = []

    # Array that represents the best time.
    best_time = []

    # Array with boolean values to test if the numbers can be drawn.
    # They can't be drawn when the number is zero.
    can_draw = []

    # Event id.
    MILLISEC_PASSED_EVENT = pygame.USEREVENT + 1

    # Get images from database.
    clock = DatabaseReceiver.get_number_img("Klok", "Klok")
    no_time_line = DatabaseReceiver.get_number_img("No_time", "No_time")

    # The x coordinate the best_time and timer should start to draw.
    timer_start_x = 820

    def __init__(self):
        # Make an array with the hundreds, tens, ones and tenths.
        # Every number should be zero at the start of the level.
        self.time = [0, 0, 0, 0]

        # This array is to determine if the number can be drawn on the
        # surface.
        # Because we only want to draw the number
        # if it is > 0. To make it look better.
        self.can_draw = [False, False, False, True]

        # Get all the images of the numbers
        # from the database and put it in the numbers array.
        for x in range(0, 10):
            self.numbers.append(DatabaseReceiver.get_number_img
                                ("Big", "hud_" + str(x)))

        # Get all the images of the small numbers
        # from the database and put it in the numbers_small array.
        for x in range(0, 10):
            self.numbers_small.append(DatabaseReceiver.get_number_img
                                      ("Small", "hud_" + str(x)))

        # Set a timer by using the set_timer method from the
        # pygame library.
        # The first number is the event id. Every event in
        # pygame has an id.
        # Because we want to make our own event,
        # we have to define an id ourself.
        #
        # Pygame's documatation said the following :
        # It is best to use the value between
        # pygame.USEREVENT and pygame.NUMEVENTS.
        # So we use pygame.USEREVENTS + 1.
        # The second argument is the number of milliseconds should pass.
        #
        # So basically this gives every 100 milliseconds
        # an event back with id: pygame.USEREVENTS + 1.
        pygame.time.set_timer(self.MILLISEC_PASSED_EVENT + 1, 100)

    def update(self):
        # Get all the pygame events by using pygame.event.get().

        for event in pygame.event.get():
            # Check with event.type if it is our event we made in
            # the init.
            # (pygame.USEREVENT + 1)
            if event.type == self.MILLISEC_PASSED_EVENT + 1:
                # Increase the 4th number with 1.
                # So that every 100 milliseconds the
                # 4th number will increase by 1. Like a timer.
                self.time[3] += 1

        # Fourth number:
        # If the 4th number is bigger then 9. (so it's ten)
        if self.time[3] > 9:
            # Increase the 3th number by one.
            self.time[2] += 1

            # Set the 4th number back to zero.
            self.time[3] = 0

            # And now that the 3th number is higher than zero,
            # we can draw it.
            self.can_draw[2] = True

        # Thirth number:
        # If the 3th number is bigger then 9. (so it's ten)
        if self.time[2] > 9:

            # Increase the 2nd number by one.
            self.time[1] += 1

            # Set the 3th number back to zero.
            self.time[2] = 0

            # And now that the 3th number is higher than zero,
            # we can draw it.
            self.can_draw[1] = True

        # Second number:
        # If the 2th number is bigger then 9. (so it's ten)
        if self.time[1] > 9:

            # Increase the 1st number by one.
            self.time[0] += 1

            # Set the 2nd number back to zero.
            self.time[1] = 0

            # And now that the 3th number is higher than zero,
            # we can draw it.
            self.can_draw[0] = True

        # First number:
        # If the 1th number is bigger then 9. (so it's ten)
        if self.time[0] > 9:
            # Reset the time. So the time will reset when its over 999.
            self.reset_time()

    # Reset all the numbers to zero.
    def reset_time(self):
        self.time[0] = 0
        self.time[1] = 0
        self.time[2] = 0
        self.time[3] = 0

    # Draw every object on the surface.
    def draw(self):
        self.draw_clock()
        self.draw_timer()
        self.draw_best_time()

    # Draw the gray clock.
    def draw_clock(self):
        Artist.draw_textures(self.clock, (770, 50))

    def draw_timer(self):
        # The x coordinate the image should start to draw.
        x = self.timer_start_x

        for i in range(0, 4):
            if self.can_draw[i]:
                # If it's the last number (tenths),
                # it should be drawn with less space and the y value
                # higher.
                if i == 3:
                    # Set the space between the 3th and 4th number.
                    x += 6

                    # Draw the last number.
                    Artist.draw_textures(self.numbers_small[self.time[i]],
                                         (x, 75))
                    break
                # Draw a number.
                Artist.draw_textures(self.numbers[self.time[i]],
                                     (x, 60))

            # Set the space between the images.
            x += 30

    # Calculate the best time and put it in the database.
    def save_best_time(self, level):
        # Multiple every number times what they represent.
        # The first number belongs to the 'hundreds',
        # so we do it times 100 etc.
        # We need to calculate the current time and the current
        # best time.
        time_temp = self.time[0] * 100 + self.time[1] * 10 + self.time[2] + (
            self.time[3] * 0.1)
        best_time_temp = self.best_time[0] * 100 + self.best_time[1] * 10 + (
            self.best_time[2] + self.best_time[3] * 0.1)

        # If the time is less then the current best time.
        # Put it in the database.
        # So you actually are faster then the current.
        #
        # Also put it in the database when the best_time is zero.
        # So it also saves when it's the first time you completed
        # the level.
        if time_temp < best_time_temp or best_time_temp == 0:
            # Save the time in the database.
            DatabaseReceiver.save_timer(str(self.time[0]), str(self.time[1]),
                                        str(self.time[2]), str(self.time[3]),
                                        str(level))

    # Get the best time from database and put it in the best_time array.
    def load_best_time(self, level):
        self.best_time = DatabaseReceiver.load_timer(str(level))

    def draw_best_time(self):
        # The x coordinate the image should start to draw.
        x = self.timer_start_x

        # If the best time is zero (so there isn't a beset time yet),
        # draw an image of a dash.
        if self.best_time[0] == 0 and self.best_time[1] == 0 \
                and self.best_time[2] == 0 and self.best_time[3] == 0:
            Artist.draw_textures(self.no_time_line, (x + 50, 700))

        for i in range(0, 4):
            # If it's the last number (tenths),
            # it should be drawn with less space and the y value higher.
            if i == 3:
                # Set the space between the 3th and 4th number.
                x += 6

                # Draw the last number.
                # Only when the number isn't zero.
                # So we don't see the numbers before it.
                if self.best_time[i] != 0:
                    Artist.draw_textures(self.numbers_small[self.best_time[i]],
                                         (x, 715))
                break

            # Draw the first three numbers.
            # Only when the number isn't zero too.
            if self.best_time[i] != 0:
                Artist.draw_textures(self.numbers[self.best_time[i]], (x, 700))

            # Set the space between the images.
            x += 30

    # Rest the best time in the database and on the game's surface.
    def reset_best_time(self, level):
        DatabaseReceiver.reset_timer()
        self.load_best_time(level)
