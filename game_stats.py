
class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.highest_score = 0

        # reset stats
        self.reset_stats()

    def reset_stats(self):
        self.lives_remaining = self.settings.maximum_lives
        self.game_active = False
        self.score = 0
        self.alien_speed = self.settings.alien_speed_default

        self.rounds_count = self.settings.rounds_count_default
        self.generation_time = 40
