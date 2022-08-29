import sys
# ^ we use tools from the sys module to close our game window, when the player quits

import pygame
# ^ The pygame module contains the functionality we need to make a game

class AlienInvasion:
    """ Overall class to manage game assests and behaviors """

    def __init__(self):
        """ Initalize the game and create ingame resources """
        pygame.init()
        # ^ the pygame.init() functino intializes the background settings that pygame needs to work

        self.screen = pygame.display.set_mode((1000, 500))
        # ^ here we call on pygame.display.set_mode() to create a window to draw the games graphics
        # ^ the (1200, 800) is a tuple that defineds the dimensions of the window
        # ^ this tuple is in pixels and reads (width, height)
        # ^ lastly we set these values to the attribute self.screen, so we can call on it later

        # The object we assigned to self.screen is called a 'surface'. This is a part of the screen
        # where a game element can be displayed. Each element of the game can be it's own surface
        # when we activate the games animation loop, the surfaces will be redrawn on every pass through
        # so it can respond to user input

        pygame.display.set_caption("Alien Invasion")
        # ^ pygame.display.set_caption titles our game window 

        # set a background color
        self.bg_color = (3, 19, 43)
        # ^ colors in pygame are specified by RGB values


    def run_game(self):
    # ^ The game is controlled by this run_game method
        """ Start the main loop of the game """
        while True:
        # ^ The while loop contains an event loop and code that manages screen updates

            for event in pygame.event.get():
            # ^ an event is an actions the user performs while playing the game
            # ^ such as hitting a key or moving the mouse
            # ^ the loop 'listens' for events, then performs the apropriate action based on the event
                if event.type == pygame.QUIT:
                # ^ one example is the if statement here
                # ^ if the event of the user hitting the windows close button occurs
                # ^ the sys.exit() fucntion will activate, closing the game
                    sys.exit()
                # ^ The above code watches for keyboard and mouse movements

            # redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            # ^ here we use fill() to fill the screen surface with our specified background color

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

