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
