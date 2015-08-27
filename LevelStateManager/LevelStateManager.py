from MainMenu.MainMenu import *
from Level2State import *
from Level3State import *
from EndDemo import *
from Timer import *
import sys

# Author: Richard Jongenburger


class LevelStateManager:
    # Explanation of the LevelStateManager:
    # This class controls and keeps track of the current level state.
    # The main purpose of this class
    # is to call the run method when a new state is created.
    # And to call the update and draw method every frame of the current level.
    #
    # There are the following states: MainMenu, OptionsMenu, Level1State,
    # Level2State, Level3State, Level4State, EndDemo.
    # The states variable holds the current state.
    #
    # Each class is given a reference to this class
    # so the states can switch from state in their class.
    # More info in the report.

    # Holds the current state. (object)
    states = None
    level_state = None

    # Int variable to hold the current level.
    # Handy to keep track of it.
    level = 1

    # This variable is used to hold the mainMenu.
    # It's necessary because we need to pass the mainMenu to level1.
    main_menu = None

    # Keep track of the players health.
    # All the levels have acces to this variable.
    player_health = 3

    # Variable for the current jump sound volume.
    # So we can set that according to the music level from the option menu.
    jump_sound_volume = 0

    # Variable to test whether you can save the best time.
    # It's needed cause you can't save it when you skip the level by pressing E
    # on your keyboard.
    can_save_best_time = True

    def __init__(self):
        # The first state is the MainMenu.
        self.states = MainMenu(self)

        # Set a reference to the main_menu in the main_menu veriable.
        self.main_menu = self.states

        # Call the run method of the MainMenu class.
        self.states.run()

    def run(self):
        # Call the run method of the current state.
        self.states.run()

    def update(self):
        # Call the update method of the current state.
        self.states.update()

        # Check whether the current state isn't the MainMenu.
        if not isinstance(self.states, MainMenu):
            # Event handling:
            # With pygame.event.get(),
            # you get all of the mouse/keyboard
            # input events in pygame's event queue.
            # Those events are automatically removed from the queue,
            # when you call pyagme.event.get() method.
            # The pygame.KEYDOWN argument ensures that
            # only the pygame.KEYDOWN events are removed.
            # The pygame.KEYDOWN event means that you
            # have a keyboard button down.
            # So it gets all the keyboard down events.
            for event in pygame.event.get(pygame.KEYDOWN):
                # If the KEYDOWN event is an E (E on your keyboard.)
                if event.key == pygame.K_e:
                    # You can't save the time.
                    self.can_save_best_time = False
                    # Open the next level.
                    self.next_level()
                # If the KEYDOWN event is an R (R on your keyboard.)
                if event.key == pygame.K_r:
                    # Reset the best time.
                    self.states.reset_best_time()

    def draw(self):
        # Call the draw method of the current state.
        self.states.draw()

    # This method opens the next level.
    def next_level(self):
        # Call the save_best_time method in the timer
        # class when the can_save_best_time boolean is True.
        if self.can_save_best_time:
            self.states.timer.save_best_time(self.level)
        else:
            # Set the can_save_best_time variable
            # back to True. So if you can't save the best time this level,
            # you can save the best time the next level.
            self.can_save_best_time = True
        # Increase the level.
        self.level += 1

        # Open the EndDemo level when the current level is five.
        if self.level == 5:
            self.states = EndDemo()
            self.states.run()
        # If it's below five, open the next level.
        else:
            # Create an object of the current level.
            self.states = getattr(sys.modules[__name__], 'Level' + str(
                self.level) + 'State')(self, self.main_menu)
            self.states.run()

        # Sets the volume level of the jump sound.
        self.set_jump_sound(self.jump_sound_volume)

    def reset_level(self):
        # Create a new object of the
        # current level and set it as the current state.
        # With getattr method we get the attribute so we can actually
        # call the class.
        self.states = getattr(sys.modules[__name__], 'Level' +
                              str(self.level) + 'State')(self, self.main_menu)
        # Call the run method of the current state.
        self.states.run()
        # Sets the volume level of the jump sound.
        self.set_jump_sound(self.jump_sound_volume)

    def open_level1(self):
        # Set the current level as 1.
        self.level = 1
        # Create a Level1State object and set it as the current state.
        self.states = Level1State(self, self.main_menu)
        # Call the run method of the current state.
        self.states.run()
        # Set the jump sounds volume level.
        self.set_jump_sound(self.jump_sound_volume)

    def set_jump_sound(self, volume):
        self.jump_sound_volume = volume

        # If the current state isn't EndDemo, set the jump sound volume level.
        if not isinstance(self.states, EndDemo):
            self.states.player.jump_sound.set_volume(volume)
