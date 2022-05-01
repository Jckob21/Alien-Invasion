import pygame.font


class Scoreboard:
    """Class to handle Scoreboard"""
    def __init__(self, ai_game):
        """Initialize a scoreboard"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self._prep_scoreboard()

    def _prep_scoreboard(self):
        """Turn the text into an image and center it"""
        # get the score
        score = str(self.game_stats.score)

        self.scoreboard_image = self.font.render(score, True)
        self.scoreboard_image_rect = self.scoreboard_image.get_rect()
        self.scoreboard_image_rect.topright = self.screen.topright
