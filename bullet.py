import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Creates an instance of Bullet using a reference to Alien Invasion game"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and correct the position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the position as decimal value.
        self.y = float(self.rect.y)

    def draw_bullet(self):
        """Draws the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Update the bullet attributes"""
        # update decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y
