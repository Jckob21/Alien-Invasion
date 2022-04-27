import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing an alien"""
    def __init__(self, ai_game):
        """Creates an instance of an alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image
        self.image = pygame.image.load('assets/alien.bmp')
        self.rect = self.image.get_rect()

        # Place the alien in the top left of the screen by default
        self.rect.topleft = (self.rect.width, self.rect.height)

        # Create variables to handle the movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_alien(self):
        """Draws an item"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the alien attributes"""
        self.y += self.settings.alien_speed
        self.rect.y = self.y
