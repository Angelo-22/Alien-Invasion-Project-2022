import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from a ship """

    def __init__(self, ai_game):
        """ create a bullet object at the ships current position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet object at (0, 0), then move it to the current position
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midtop = ai_game.ship.ship_rect.midtop

        # store the bullets position as a decimal value
        self.bullet_y = float(self.bullet_rect.y)

    def update(self):
        """ Move the bullet up the screen """
        # Update the decimal position of the bullet
        self.bullet_y -= self.settings.bullet_speed
        # Update the rect position
        self.bullet_rect.y = self.bullet_y

    def draw_bullet(self):
        """ Draw the Bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)