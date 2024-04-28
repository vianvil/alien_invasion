import sys
import pygame

class AlienInvasion:
    """Main class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1600, 800))
        pygame.display.set_caption("Alien Invasion")

        #Setting the background color
        self.bg_color = (230, 230, 100)

    
    def run_game(self):
        """Start the main loop for the game (How the game will run, and how to exit)"""
        while True:
            #Monitor keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redrawing the screen each pass
            self.screen.fill(self.bg_color)
            
            #displaying the drawn screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #Instance of game, and running it
    ai = AlienInvasion()
    ai.run_game()