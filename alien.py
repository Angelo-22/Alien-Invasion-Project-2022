import pygame

from pygame.sprite import Sprite

class Aliens(Sprite):
    """ A class to represent a single alien in a fleet """

    def __init__(self, ai_game):
        """ Initialize the alien and set it's starting position """

        super().__init__()
        self.screen =ai_game.screen
        self.settings = ai_game.settings

        #Load the image for the alien and set it's rectangle value
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.alien_x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x



