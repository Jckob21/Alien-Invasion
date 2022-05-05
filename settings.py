class Settings:
    """Stores all setting for the game."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # alien settings
        self.alien_speed_default = 0.1

        # game related settings
        self.maximum_lives = 3

        # scoring settings
        self.alien_point_reward = 50
        self.alien_hit_ground_deduction = 20

        # fleet generation settings
        self.initial_generation_time = 2.0
        self.rounds_count_default = 5

