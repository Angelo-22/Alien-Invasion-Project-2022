import sys
# ^ we use tools from the sys module to close our game window, when the player quits

import pygame
# ^ The pygame module contains the functionality we need to make a game

from settings import Settings
# ^ this imports the Settings class from settings.py

from ship import Ship
# import  the Ship class

from bullet import Bullet

from alien import Aliens

class AlienInvasion:
    """ Overall class to manage game assests and behaviors """

    def __init__(self):
        """ Initalize the game and create ingame resources """
        pygame.init()
        # ^ the pygame.init() functino intializes the background settings that pygame needs to work
        self.settings = Settings()
        # ^ this creates an instance of the settings class that we can call in all future modules 
        # in our AlienInvasion class. Letting us access values like screen_width/height and bg_color

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # ^ here we call on pygame.display.set_mode() to create a window to draw the games graphics
        # ^ the (10000, 500) is a tuple that defineds the dimensions of the window
        # ^ this tuple is in pixels and reads (width, height)
        # in this new iteration we set the screen to full screen mode
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

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
    # ^ The game is controlled by this run_game method
        """ Start the main loop of the game """
        while True:
        # ^ The while loop contains an event loop and code that manages screen updates

            self._check_events()
            # call the method that checks for events, like if the windowns been closed

            self.ship.update_ship_position()

            self._update_bullets()

            self._update_aliens()

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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # ^ KEYUP refers to when a key is released
                self._check_keyup_events(event)
            # ^ The above code watches for keyboard and mouse movements

    def _check_keydown_events(self, event):
        """ Respond to when the key is pressed down """
        if event.key == pygame.K_RIGHT:
            self.ship.ship_move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.ship_move_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to when the key is released """
        if event.key == pygame.K_RIGHT:
            self.ship.ship_move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.ship_move_left = False

    def _fire_bullet(self):
        """ create a new bullet and add it to the group of bullets """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets """
        # Update bullets position
        self.bullets.update()
        # get rid of bullets that have disappear 
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """ create the fleet of aliens """
        # create an alien and find the number of aliens in a row
        # Spacing between each alien is an alien width
        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size

        # deterimine the number of aliens that will fit in a single row
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows that can fit on my screen size
        ship_height = self.ship.ship_rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)


        # create a full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """ create an alien and place it in a row """
        # create an alien and place it in the row
        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """ Update he position of all aliens in the fleet """
        self.aliens.update()
        



    def _update_screen(self):
        """ Redraw the screen on each pass through the loop """
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        # ^ here we use fill() to fill the screen surface with our specified background color

        self.ship.blitme()
        # after filling the background we draw the ship on the screen by calling ship.blitme() 
        # this draws the ship on top of the background

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

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

