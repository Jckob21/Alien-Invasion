import pygame


class Ship:
    """A class to manage a ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('assets/spaceship.bmp')
        self.rect = self.image.get_rect()

        # Place the ship at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Create variables to handle the movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates ship's attributes. Relies upon it's state."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # adapt the image variable to the new value
        self.rect.x = self.x
        self.rect.y = self.y