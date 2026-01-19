import pygame

class DisplaySettings:
    def __init__(self):
        self.fullscreen = False
        self.screen_width = 1280
        self.screen_height = 720
    
    def toggle_fullscreen(self):
        """Toggle between windowed and fullscreen mode"""
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        return screen
    
    def is_fullscreen(self):
        """Check if currently in fullscreen mode"""
        return self.fullscreen
