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

        self.generation_time = 40
        self.time = 0

        self.round = 0
        self.rounds_count = self.settings.rounds_count_default

    def run(self):
        """Generate fleet every 4 seconds"""
        while not self.stop_flag:
            if self.game_stats.game_active:
                print(f"time: {self.time} / {self.generation_time}")
                sleep(0.1)
                self.time += 1
                if self.time >= self.generation_time:
                    self._generate()

    def _generate(self):
        self.ai_game._create_fleet(self.ai_game.fleet_positions, -100)
        self.round += 1
        if self.round >= self.rounds_count:
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
            print("Round bigger difficulty")
        elif number == 2:
            print("Generation time decreased")


    def reset_round(self):
        self.time = self.generation_time
        self.round = 0
