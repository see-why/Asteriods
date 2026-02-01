import pygame

class ColorTheme:
    """Color scheme definitions"""
    CLASSIC = {
        "background": (0, 0, 0),
        "player": (0, 255, 0),
        "asteroid": (255, 255, 255),
        "shot": (255, 255, 255),
        "ui": (255, 255, 255)
    }
    
    NEON = {
        "background": (10, 0, 30),
        "player": (0, 255, 255),
        "asteroid": (255, 0, 255),
        "shot": (255, 255, 0),
        "ui": (0, 255, 255)
    }
    
    RETRO = {
        "background": (20, 20, 20),
        "player": (255, 200, 0),
        "asteroid": (200, 100, 50),
        "shot": (255, 150, 0),
        "ui": (255, 200, 0)
    }
    
    OCEAN = {
        "background": (0, 20, 40),
        "player": (0, 200, 255),
        "asteroid": (100, 200, 255),
        "shot": (200, 255, 255),
        "ui": (150, 220, 255)
    }

class ThemeManager:
    def __init__(self):
        self.themes = {
            "classic": ColorTheme.CLASSIC,
            "neon": ColorTheme.NEON,
            "retro": ColorTheme.RETRO,
            "ocean": ColorTheme.OCEAN
        }
        self.current_theme = "classic"
    
    def set_theme(self, theme_name):
        """Set active color theme"""
        if theme_name in self.themes:
            self.current_theme = theme_name
    
    def get_color(self, element):
        """Get color for specific element"""
        theme = self.themes.get(self.current_theme, ColorTheme.CLASSIC)
        return theme.get(element, (255, 255, 255))
    
    def get_theme_names(self):
        """Get list of available themes"""
        return list(self.themes.keys())
