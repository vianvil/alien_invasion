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

        #Ship settings
        self.settings = ai_game.settings

        #Storing ship's horizontal position as a float since speed setting is a float, so we can work with
        self.x = float(self.rect.x)

    
    def update(self):
        """Updating ship position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x (this controls the position of the ship)
        self.rect.x = self.x

   
    def blitme(self):
        """Drawing the ship"""
        self.screen.blit(self.image, self.rect)