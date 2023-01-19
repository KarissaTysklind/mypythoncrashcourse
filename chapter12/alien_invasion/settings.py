from random import randint

class Settings():
    #stores all settings for AI

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (16, 15, 56)

         # Ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_colour = (0, 255, 0)
        self.bullets_allowed = 3

        # Star Settings
        self.star_width = 2
        self.star_height = 2
        self.star_color = (255, 255, 255)
        self.star_separation = 50
        self.stars_allowed = 50

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quicly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 15
        self.bullet_speed = 30
        self.alien_speed = 15
        self.star_speed = 3.0

        #fleet_direction and star_direction of 1 represents right; -1 respresents left.
        self.fleet_direction = 1
        self.star_direction = -1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        


