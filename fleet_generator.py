import threading
from time import sleep
import random

class FleetGenerator(threading.Thread):

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
        self.ai_game = ai_game
        self.stop_flag = False

        self.time = 0

        self.round = 0

    def run(self):
        """Generate fleet every 4 seconds"""
        while not self.stop_flag:
            if self.game_stats.game_active:
                sleep(0.1)
                self.time += 1
                if self.time >= self.game_stats.generation_time:
                    self._generate()

    def _generate(self):
        self.ai_game._create_fleet(self.ai_game.fleet_positions, -100)
        self.round += 1
        if self.round >= self.game_stats.rounds_count:
            self.round = 0
            sleep(3)
            self._delegate_difficulty_increase(random.randint(0, 3))
        # self.game_stats.alien_speed += 0.01
        self.time = 0

    def _delegate_difficulty_increase(self, number):
        if number == 0:
            print(f"Alien speed up difficulty")
            self.game_stats.alien_speed += 0.05
        elif number == 1:
            print("Round longer difficulty")
            self.game_stats.rounds_count += 2

        elif number == 2:
            print("Generation time decreased")
            self.game_stats.generation_time -= 4
            if self.game_stats.generation_time <= 0:
                self.game_stats.generation_time = 2


    def reset_round(self):
        self.time = self.game_stats.generation_time
        self.round = 0
