import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """This class is the main class of the Alien Invasion game. You can start the game by calling run_game."""
    def __init__(self):
        """Creates an instance of AlienInvasion. Instantiates a settings object, sets a screen, and handles the ship
        and attributes."""
        pygame.init()
        self.settings = Settings()

        # set screen to full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Create a ship
        self.ship = Ship(self)

        # Create a list of entities
        self.bullets = pygame.sprite.Group()
        self.bullets_counter = 0

        self.aliens = pygame.sprite.Group()
        self.aliens.add(Alien(self))

        pygame.display.set_caption("alien invasion")

    def run_game(self):
        """Runs the main loop which:
        "   - handles occurring events
        "   - updates screen
        "   - updates bullets
        "   - updates the ship"""
        while True:
            self._check_events()
            self._update_screen()
            self.bullets.update()
            self.aliens.update()
            self.ship.update()
            self._delete_bullets_outside_map()

    def _check_events(self):
        """Checks for existing events and handles them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_key_down(event)
            elif event.type == pygame.KEYUP:
                self._handle_key_up(event)

    def _handle_key_up(self, event):
        """Handles key up events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _handle_key_down(self, event):
        """Handles key down events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _update_screen(self):
        """Updates screen according to current state of the game."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.draw_alien()

        pygame.display.flip()

    def _fire_bullet(self):
        """Fires bullet on the top of the sprite of the ship."""
        if self.bullets_counter < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)
            self.bullets_counter += 1

    def _delete_bullets_outside_map(self):
        """Deletes all bullets that are outside of the map"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                self.bullets_counter -= 1


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
