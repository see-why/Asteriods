import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

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



        


