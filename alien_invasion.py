import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Creating an instance of the ship in the game Main class
        self.ship = Ship(self)


    
    def run_game(self):
        """Start the main loop for the game (How the game will run, and how to exit)"""
        while True:
            #Monitor keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redrawing the screen each pass
            self.screen.fill(self.settings.bg_color)

            #Drawing the ship in the game
            self.ship.blitme()
            
            #displaying the drawn screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #Instance of game, and running it
    ai = AlienInvasion()
    ai.run_game()