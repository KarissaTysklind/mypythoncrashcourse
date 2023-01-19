import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Initialize the alien and set its starting position."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image
        self.image = pygame.image.load('chapter12/alien_invasion/images/alien_small_pink.png')
        self.rect = self.image.get_rect()

        # Start alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the alien right or left"""
        self.x += (self.settings.alien_speed * 
                        self.settings.fleet_direction)
        self.rect.x = self.x


