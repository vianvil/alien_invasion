import pygame

class Ship:
    """Class to manage all things ship related."""

    def __init__(self, ai_game):
        """Initialize the ship and setting starting location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draws the ship"""
        self.screen.blit(self.image, self.rect)