import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing an alien"""
    def __init__(self, ai_game, x_topmid = 100, y_topmid = 100):
        """Creates an instance of an alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image
        self.image = pygame.image.load('assets/alien.bmp')
        self.rect = self.image.get_rect()

        # Place the alien in the top left of the screen by default
        self.rect.midtop = (x_topmid, y_topmid)

        # Create variables to handle the movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_alien(self):
        """Draws an item"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the alien attributes"""
        self.y += self.game_stats.alien_speed
        self.rect.y = self.y
