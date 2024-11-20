import sys
import pygame

class AlienInvasion:
    """Main class used to manage game assets and behavior."""

    def __init__(self):
        """Initialize pygame to allow us to use it's tools."""
        pygame.init()

        """Creating the display window and setting dimensions and name."""
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Starts the game loop."""
        while True:
            # Keyboard and mouse events handlers.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ! Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Create an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()