import pygame.font


class Scoreboard:
    """Class to handle Scoreboard"""
    def __init__(self, ai_game):
        """Initialize a scoreboard"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self.font_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Get the score, turn it into an image and align it to the right side."""
        # get the score
        score_str = str(self.game_stats.score)

        self.score_image = self.font.render(score_str, True, self.font_color, self.settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.top = 20
        self.score_image_rect.right = self.screen_rect.right - 20

    def prep_highest_score(self):
        """Get the highest score, turn it into an image and center it."""


    def draw_scoreboard(self):
        """Draw the scoreboard on the screen"""
        self.screen.blit(self.score_image, self.score_image_rect)