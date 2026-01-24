import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = random.uniform(-50, 50)
        self.asteroid_type = self.determine_type(radius)
        self.color = self.get_color()
        self.health_multiplier = self.get_health_multiplier()
        self.trail_positions = []
        self.max_trail_length = 5
    
    def determine_type(self, radius):
        """Determine asteroid type based on radius"""
        if radius >= ASTEROID_MIN_RADIUS * 3:
            return "large"
        elif radius >= ASTEROID_MIN_RADIUS * 2:
            return "medium"
        else:
            return "small"
    
    def get_color(self):
        """Get color based on asteroid type"""
        colors = {
            "large": "red",
            "medium": "orange",
            "small": "white"
        }
        return colors.get(self.asteroid_type, "white")
    
    def get_health_multiplier(self):
        """Get health multiplier based on type"""
        multipliers = {
            "large": 2.0,
            "medium": 1.5,
            "small": 1.0
        }
        return multipliers.get(self.asteroid_type, 1.0)

    def draw(self, screen):
        # Draw trail for fast-moving asteroids
        if self.velocity.length() > 100:
            for i, pos in enumerate(self.trail_positions):
                alpha = int(100 * (i / max(1, len(self.trail_positions))))
                pygame.draw.circle(screen, self.color, pos, self.radius // 2, 1)
        
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
       # Update trail
       if self.velocity.length() > 100:
           self.trail_positions.append(pygame.Vector2(self.position.x, self.position.y))
           if len(self.trail_positions) > self.max_trail_length:
               self.trail_positions.pop(0)
       
       self.position += self.velocity * dt
       self.rotation += self.rotation_speed * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rotate_angle = random.uniform(20, 50)
        first_rotate_vector = self.velocity.rotate(rotate_angle)
        second_rotate_vector = self.velocity.rotate(-rotate_angle)

        other_radius = self.radius - ASTEROID_MIN_RADIUS
        small_asteroid = Asteroid(self.position.x, self.position.y, ASTEROID_MIN_RADIUS)
        small_asteroid.velocity = first_rotate_vector * 2.0
        other_asteroid = Asteroid(self.position.x, self.position.y, other_radius)
        other_asteroid.velocity = second_rotate_vector * 1.2



        


