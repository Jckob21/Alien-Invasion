
class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings

        # reset stats
        self.reset_stats()

    def reset_stats(self):
        self.lives_remaining = self.settings.maximum_lives
