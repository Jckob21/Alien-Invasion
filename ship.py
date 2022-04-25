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

        # Start the ship at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

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
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed

        # adapt the variable to the new value
        self.rect.x = self.x
        self.rect.y = self.y