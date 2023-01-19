import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    #initialise ship
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
    
        #load ship
        self.image = pygame.image.load('chapter12/alien_invasion/images/spaceship_grey.png')
        self.rect = self.image.get_rect()

        #start new ship at the bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
            
        #movement flag
        self.moving_right = False
        self.moving_left = False

       
    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    #draw ship at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def centre_ship(self):
        """Centre the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
