import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """This class is the main class of the Alien Invasion game. You can start the game by calling run_game."""
    def __init__(self):
        """Creates an instance of AlienInvasion. Instantiates a settings object, sets a screen, and handles the ship
        and attributes."""
        pygame.init()
        self.settings = Settings()

        # uncomment to set screen to full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 700))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Create a game stats object
        self.game_stats = GameStats(self)

        # Create a button object
        self.start_button = Button(self, "START")

        # Create scoreboard object
        self.scoreboard = Scoreboard(self)

        # Create a ship
        self.ship = Ship(self)

        # Create a list of entities
        self.bullets = pygame.sprite.Group()
        self.bullets_counter = 0

        self.aliens = pygame.sprite.Group()

        # Create a fleet of aliens
        self.fleet_positions = self._get_fleet_positions()
        self._create_fleet(self.fleet_positions, 100)

        pygame.display.set_caption("alien invasion")

    def run_game(self):
        """Runs the main loop which:
        "   - handles occurring events
        "   - updates screen
        "   - updates bullets
        "   - updates the ship"""
        while True:
            self._check_events()

            if self.game_stats.game_active:
                self.bullets.update()
                self.aliens.update()
                self._check_collisions()
                self.ship.update()
                self._delete_bullets_outside_map()
                self._check_aliens_touch_the_bottom()

            self._update_screen()

    def _check_events(self):
        """Checks for existing events and handles them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_key_down(event)
            elif event.type == pygame.KEYUP:
                self._handle_key_up(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_down()

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

    def _handle_mouse_down(self):
        """Handles mouse down event"""
        mouse_position = pygame.mouse.get_pos()
        if self.start_button.rect.collidepoint(mouse_position) and not self.game_stats.game_active:
            self._on_start_button_clicked()

    def _on_start_button_clicked(self):
        """Restarts the game"""
        self.game_stats.reset_stats()
        self.game_stats.game_active = True
        # hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Updates screen according to current state of the game."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.draw_alien()

        # Print the button if the game is paused
        if not self.game_stats.game_active:
            self.start_button.draw_button()

        self.scoreboard.draw_scoreboard()

        # Update the image view
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

    def _get_fleet_positions(self):
        """Method finds x positions for an aliens fleet"""
        # helper object to get information about the image
        alien = Alien(self)
        alien_width = alien.rect.width

        # calculate fleet positions
        space_available = self.settings.screen_width - alien_width
        aliens_available = space_available // (1.2 * alien_width)

        # create positions for the aliens, starting at alien_width
        positions = [alien_width]
        i = 0
        while i < aliens_available - 1:
            positions.append(positions[i] + 1.2 * alien_width)
            i += 1
        return positions

    def _create_fleet(self, x_positions, y):
        """Creates a fleet of aliens"""
        for x_position in x_positions:
            self.aliens.add(Alien(self, x_position, y))

    def _check_collisions(self):
        """Checks collisions in the game"""
        # check if any bullet hit the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        self.bullets_counter -= len(collisions)
        self.game_stats.score += len(collisions) * self.settings.alien_point_reward
        self.scoreboard.prep_score()

        # check if any alien collided with the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._handle_ship_dead()

    def _handle_ship_dead(self):
        """Handles collision of ship and an alien"""
        # subtract lives_remaining
        self.game_stats.lives_remaining -= 1

        if self.game_stats.lives_remaining == 0:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)
            # update highest score
            if self.game_stats.score > self.game_stats.highest_score:
                self.game_stats.highest_score = self.game_stats.score
                self.scoreboard.prep_highest_score()

        self._regenerate_fleet()

    def _regenerate_fleet(self):
        """Regenerates aliens, centers the ship"""

        # Empty aliens
        self.aliens.empty()
        self.bullets.empty()

        # Create new fleet and center the ship
        self._create_fleet(self.fleet_positions, 100)
        self.ship.center_ship()

        # Pause
        sleep(0.5)

    def _check_aliens_touch_the_bottom(self):
        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self.aliens.remove(alien)
                # update score and scoreboard image
                self.game_stats.score -= self.settings.alien_hit_ground_deduction
                self.scoreboard.prep_score()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
