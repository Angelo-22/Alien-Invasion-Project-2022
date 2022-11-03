# we are creating a seperate file and clas for our games settings, we do this mainly to have one resource
# to call our settings from, instead of have dispersed through out our main program
# or piled at the top as just a bunch of resources
# this will also help for the future as it will make it easy to add settings for our game as it becomes
# more complex

class Settings:
    """ A class to store the settings for the game """

    def __init__(self):
        """ Initialize the games settings """

        #Screen Settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (3, 19, 43) #colors in python are specified as RGB values

        # Ship Settings
        self.ship_speed = 1.5
        self.lives = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (163, 46, 46)
        # ^ these settings create a maroon bullet that is 3 pixels wide and 15 pixels high
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet direction of 1 = right, -1 = left
        self.fleet_direction = 1
