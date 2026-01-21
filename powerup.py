import pygame
import random
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(CircleShape):
    containers = ()
    
    def __init__(self, x, y, powerup_type):
        super().__init__(x, y, 15)
        self.powerup_type = powerup_type
        self.lifetime = 10  # Power-up stays on screen for 10 seconds
        self.colors = {
            "shield": "cyan",
            "rapid_fire": "yellow",
            "health": "green",
            "extra_life": "red"
        }
    
    def draw(self, screen):
        color = self.colors.get(self.powerup_type, "white")
        pygame.draw.circle(screen, color, self.position, self.radius, 3)
        # Draw inner circle for visual effect
        pygame.draw.circle(screen, color, self.position, self.radius // 2, 0)
    
    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
    
    @classmethod
    def spawn_random(cls, powerup_type=None):
        """Spawn a random power-up at a random location"""
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        
        if powerup_type is None:
            powerup_type = random.choice(["shield", "rapid_fire", "health", "extra_life"])
        
        return cls(x, y, powerup_type)
