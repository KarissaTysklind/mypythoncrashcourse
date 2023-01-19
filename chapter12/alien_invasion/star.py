import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.star_color

        # Create a star rect at (0,0).
        self.rect = pygame.Rect(0, 0, self.settings.star_width,
            self.settings.star_height)

        # Store star's position bottom left.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star position
        self.y = float(self.rect.y)

    def update(self):
        # Update decimal position of the star.
        self.y += self.settings.star_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_star(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    