import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.asteroid_type = self.determine_type(radius)
        self.color = self.get_color()
        self.health_multiplier = self.get_health_multiplier()
    
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
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt

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



        


