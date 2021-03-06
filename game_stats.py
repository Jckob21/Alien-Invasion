import json

highest_score_filename = "data.txt"


class GameStats:
    """Class storing game statistics."""

    def __init__(self, ai_game):
        """Creates an instance of GameStats. Most attributes are declared in reset_stats."""
        self.settings = ai_game.settings
        self.highest_score = 0

        # reset stats
        self.reset_stats()

    def reset_stats(self):
        """Resets stats of the game."""
        self.lives_remaining = self.settings.maximum_lives
        self.game_active = False
        self.score = 0
        self.alien_speed = self.settings.alien_speed_default

        self.rounds_count = self.settings.rounds_count_default
        self.generation_time = 40

    def retrieve_saved_highest_score(self):
        """Retrieves the highest score from the file. If the file is not present, sets the highest score to 0."""
        try:
            with open(highest_score_filename, 'r') as file:
                self.highest_score = json.load(file)
        except FileNotFoundError:
            self.highest_score = 0

    def save_highest_score(self):
        """Saves the highest score in the file"""
        with open(highest_score_filename, 'w') as file:
            json.dump(self.highest_score, file)
