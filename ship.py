import pygame

class Ship:
    """A class for the ship in the game"""

    def __init__(self, ai_game):
        """Initialize the ship and setting its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Loading the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Putting ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement trackers
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """Updating ship position based on movement flags"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

   
    def blitme(self):
        """Drawing the ship"""
        self.screen.blit(self.image, self.rect)