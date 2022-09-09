import pygame
# ^ we import pygame to use some of it's module in th actually class

class Ship:
    """ A class to handle functions of the ship """

    def __init__(self, ai_game):
        # ^ use the instance of ai_game as a parameter, so that ship has access to the game resources
        # we defined in the AlienInvasion class

        """ Initialize the ship and set it's starting position """

        self.screen = ai_game.screen
        # ^ here we assign the screen to an attribute in ship, to have easy access for the other modules
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()
        # ^ here we access the screen rectagle atribute using get_rect(),
        # doing so allows us to place the ship in it's correct position on the screen

        # Load the ship and get it's rect
        self.ship_image = pygame.image.load('images/ship.bmp')
        # ^ we load the image for out ship using pygame.image.load and give it the location of the ship image
        # this function returns a surface representing the ship, that we assign to self.ship_image
        self.ship_rect = self.ship_image.get_rect()
        # with the ship loaded, we use get_rect() to get the rectangle attribute for the ship

        # store a decimal value as the ships horizontal position
        self.ship_x = float(self.ship_rect.x)

        # start each new ship at the bottom of the screen
        self.ship_rect.midbottom = self.screen_rect.midbottom

        # set movement flag for moving right
        self.ship_move_right = False
        # set movement flag for moving left
        self.ship_move_left = False

    def update_ship_position(self):
        """ Update the ships position based on movement flags """
        # update the ships x value, not the rect
        if self.ship_move_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_x += self.settings.ship_speed
            # ^ moves the ship to the right if flag is True
        if self.ship_move_left and self.ship_rect.left > 0:
            self.ship_x -= self.settings.ship_speed
            # ^ moves the ship to the left if flag is True

        # update the rect object from self.ship_x
        self.ship_rect.x = self.ship_x


    def blitme(self):
        """ Draw the ship at it's current location """
        self.screen.blit(self.ship_image, self.ship_rect)

