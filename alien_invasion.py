import sys
# ^ we use tools from the sys module to close our game window, when the player quits

import pygame
# ^ The pygame module contains the functionality we need to make a game

from settings import Settings
# ^ this imports the Settings class from settings.py

from ship import Ship
# import  the Ship class

class AlienInvasion:
    """ Overall class to manage game assests and behaviors """

    def __init__(self):
        """ Initalize the game and create ingame resources """
        pygame.init()
        # ^ the pygame.init() functino intializes the background settings that pygame needs to work
        self.settings = Settings()
        # ^ this creates an instance of the settings class that we can call in all future modules 
        # in our AlienInvasion class. Letting us access values like screen_width/height and bg_color

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # ^ here we call on pygame.display.set_mode() to create a window to draw the games graphics
        # ^ the (10000, 500) is a tuple that defineds the dimensions of the window
        # ^ this tuple is in pixels and reads (width, height)
        # ^ lastly we set these values to the attribute self.screen, so we can call on it later

        # The object we assigned to self.screen is called a 'surface'. This is a part of the screen
        # where a game element can be displayed. Each element of the game can be it's own surface
        # when we activate the games animation loop, the surfaces will be redrawn on every pass through
        # so it can respond to user input

        pygame.display.set_caption("Alien Invasion")
        # ^ pygame.display.set_caption titles our game window 

        self.ship = Ship(self)
        # ^ here we create an instance of ship, after the screen has been created
        # The Ship class needs 1 argument, and instance of AlienInvasion
        # the self arguement refers to the current instance of AlienInvasion, giving ship access to 
        # it's resources

    def run_game(self):
    # ^ The game is controlled by this run_game method
        """ Start the main loop of the game """
        while True:
        # ^ The while loop contains an event loop and code that manages screen updates

            self._check_events()
            # call the method that checks for events, like if the windowns been closed

            self._update_screen()
            # call the method that updates the screen on each pass through

    def _check_events(self):
        """ respond to keypresses and mouse events """
        for event in pygame.event.get():
        # ^ an event is an actions the user performs while playing the game
        # ^ such as hitting a key or moving the mouse
        # ^ the loop 'listens' for events, then performs the apropriate action based on the event
            if event.type == pygame.QUIT:
            # ^ one example is the if statement here
            # ^ if the event of the user hitting the windows close button occurs
            # ^ the sys.exit() fucntion will activate, closing the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # ^ KEYDOWN refers to when a key is pressed
                if event.key == pygame.K_RIGHT:
                    # moves the ship to the right, when right arrow is pressed
                    self.ship.ship_rect.x += 10
            # ^ The above code watches for keyboard and mouse movements

    def _update_screen(self):
        """ Redraw the screen on each pass through the loop """
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        # ^ here we use fill() to fill the screen surface with our specified background color

        self.ship.blitme()
        # after filling the background we draw the ship on the screen by calling ship.blitme() 
        # this draws the ship on top of the background

        pygame.display.flip()
        # ^ The above code makes the most recently drawn screen visible
        # in it's current state it redraws a blank screen everytime we loop through
        # pygame.display.flip() continuly updates the games elements, hiding the old ones
        # creating the illusion of smooth movement
    


if __name__ == "__main__":
    # The below code makes an actual game instance and runs the game
    ai = AlienInvasion()
    ai.run_game()
    # we run the game in an if statement, so the game will only run if the file is called directly

