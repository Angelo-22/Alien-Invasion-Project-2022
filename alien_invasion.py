import sys

import pygame

class AlienInvasion:
    """ Overall class to manage game assests and behaviors """

    def __init__(self):
        """ Initalize the game and create ingame resources """
        pygame.init()


        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """ Start the main loop of the game """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        # ^ The above code watches for keyboard and mouse movements

        pygame.display.flip()
        # ^ The above code makes the most recently drawn screen visible


if __name__ == "__main__":
    # The below code makes an actual game instance and runs the game
    ai = AlienInvasion()
    ai.run_game()

