import pygame.font
from ship import Ship


class Scoreboard:
    """Class to handle Scoreboard"""

    def __init__(self, ai_game):
        """Initialize a scoreboard"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        # save the reference to the game to instantiate ships later on
        self.ai_game = ai_game

        self.font_color = (30, 30, 30)
        self.highest_font_color = (120, 120, 120)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_highest_score()
        self.prep_score()
        self.prep_ships_left()

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
        highest_score_txt = str(self.game_stats.highest_score)

        self.highest_score_image = self.font.render(highest_score_txt, True, self.highest_font_color, self.settings.bg_color)
        self.highest_score_image_rect = self.highest_score_image.get_rect()
        # align it to the center of the screen
        self.highest_score_image_rect.center = self.screen_rect.center
        self.highest_score_image_rect.top = 20

    def prep_ships_left(self):
        """Create a group of ships representing lives_remaining and align it to the left top side."""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.game_stats.lives_remaining):
            ship = Ship(self.ai_game)
            self.ships.add(ship)

            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10

    def draw_scoreboard(self):
        """Draw the scoreboard on the screen"""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_image_rect)
        self.ships.draw(self.screen)
