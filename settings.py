class Settings:
    """A class for settings"""
    def __init__(self):
        """initialize the game's settings"""
        #Screen settings
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #Ship settings
        self.ship_speed = 3.0