import sys

import pygame

bg_color = (230, 230, 230)


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("alien invasion")

    def run_game(self):
        """Starts the main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(bg_color)

            pygame.display.flip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
