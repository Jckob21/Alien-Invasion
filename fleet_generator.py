import threading
from time import sleep


class FleetGenerator(threading.Thread):

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
        self.ai_game = ai_game
        self.stop_flag = False

        self.generation_time = 40
        self.time = 0

    def run(self):
        """Generate fleet every 4 seconds"""
        while not self.stop_flag:
            if self.game_stats.game_active:
                print(f"time: {self.time} / {self.generation_time}")
                sleep(0.1)
                self.time += 1
                if self.time >= self.generation_time:
                    self.ai_game._create_fleet(self.ai_game.fleet_positions, -100)
                    # self.game_stats.alien_speed += 0.01
                    self.time = 0

    def set_generation_time(self):
        self.time = self.generation_time
