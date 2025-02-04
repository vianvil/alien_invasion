import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main class used to manage game assets and behavior."""

    def __init__(self):
        """Initialize pygame to allow us to use it's tools."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        """Creating the display window and setting dimensions and name."""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create ship instance.
        self.ship = Ship(self)

    def run_game(self):
        """Starts the game loop."""
        while True:
            # Keyboard and mouse events handlers.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """End of while loop"""
            
            # Redraws the screen with the background color.
            self.screen.fill(self.settings.bg_color)
            
            # Redraws the screen with ship added.
            self.ship.blitme()

            # Makes the most recently drawn screen visible.
            pygame.display.flip()

            # Sets the frame rate for clock.
            self.clock.tick(60)

if __name__ == '__main__':
    # Create an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()