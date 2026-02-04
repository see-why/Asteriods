import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class MiniMap:
    def __init__(self, size=150):
        self.size = size
        self.position = (SCREEN_WIDTH - size - 20, 20)  # Top right corner
        self.scale_x = size / SCREEN_WIDTH
        self.scale_y = size / SCREEN_HEIGHT
    
    def draw(self, screen, player, asteroids):
        """Draw mini-map showing player and asteroid positions"""
        # Draw background
        pygame.draw.rect(screen, (50, 50, 50), (*self.position, self.size, self.size))
        pygame.draw.rect(screen, "white", (*self.position, self.size, self.size), 1)
        
        # Draw asteroids as red dots
        for asteroid in asteroids:
            map_x = self.position[0] + asteroid.position.x * self.scale_x
            map_y = self.position[1] + asteroid.position.y * self.scale_y
            pygame.draw.circle(screen, "red", (int(map_x), int(map_y)), 2)
        
        # Draw player as green dot
        map_x = self.position[0] + player.position.x * self.scale_x
        map_y = self.position[1] + player.position.y * self.scale_y
        pygame.draw.circle(screen, "green", (int(map_x), int(map_y)), 3)
