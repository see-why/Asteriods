import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, weapon_type="normal"):
        super().__init__(x, y, SHOT_RADIUS)
        self.weapon_type = weapon_type
        self.pierce_count = 3 if weapon_type == "pierce" else 0

    def draw(self, screen):
        end_pos = self.position + self.velocity.normalize() * (self.radius * 2)
        color = "cyan" if self.weapon_type == "pierce" else "white"
        pygame.draw.line(screen, color, self.position, end_pos, 2)
    
    def can_pierce(self):
        """Check if shot can pierce through asteroids"""
        if self.weapon_type == "pierce" and self.pierce_count > 0:
            self.pierce_count -= 1
            return True
        return False

    def update(self, dt):
       self.position += self.velocity * dt
