import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class AsteroidWarning:
    def __init__(self):
        self.warning_distance = 150  # Distance from screen edge to show warning
    
    def draw_warnings(self, screen, player, asteroids):
        """Draw warning indicators for off-screen asteroids"""
        for asteroid in asteroids:
            # Check if asteroid is off-screen
            if self.is_offscreen(asteroid):
                self.draw_warning_indicator(screen, player, asteroid)
    
    def is_offscreen(self, asteroid):
        """Check if asteroid is outside screen bounds"""
        margin = 50
        return (asteroid.position.x < -margin or 
                asteroid.position.x > SCREEN_WIDTH + margin or
                asteroid.position.y < -margin or 
                asteroid.position.y > SCREEN_HEIGHT + margin)
    
    def draw_warning_indicator(self, screen, player, asteroid):
        """Draw a warning indicator at screen edge"""
        # Calculate direction from player to asteroid
        direction = asteroid.position - player.position
        if direction.length() == 0:
            return
        
        direction = direction.normalize()
        
        # Calculate position on screen edge
        indicator_pos = player.position + direction * 300
        
        # Clamp to screen bounds
        indicator_pos.x = max(20, min(SCREEN_WIDTH - 20, indicator_pos.x))
        indicator_pos.y = max(20, min(SCREEN_HEIGHT - 20, indicator_pos.y))
        
        # Draw warning triangle
        size = 10
        points = [
            (indicator_pos.x, indicator_pos.y - size),
            (indicator_pos.x - size, indicator_pos.y + size),
            (indicator_pos.x + size, indicator_pos.y + size)
        ]
        pygame.draw.polygon(screen, "yellow", points)
