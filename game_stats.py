class GameStats:
    """ Track statistics from the game for things like scoring """

    def __init__(self, ai_game):
        """ Intialize the stats """
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ initialize stats that can change while the game is still running """
        self.ships_left = self.settings.lives

