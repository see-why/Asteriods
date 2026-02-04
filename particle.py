import pygame
import random
from circleshape import CircleShape

class Particle(CircleShape):
    containers = ()
    
    def __init__(self, x, y, velocity, color="white", lifetime=1.0):
        super().__init__(x, y, random.uniform(1, 3))
        self.velocity = velocity
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
    
    def draw(self, screen):
        # Fade out as particle ages by reducing brightness
        fade = self.lifetime / self.max_lifetime
        if fade > 0:
            # Convert color name to RGB and scale brightness
            base_color = pygame.Color(self.color)
            faded_color = (
                int(base_color.r * fade),
                int(base_color.g * fade),
                int(base_color.b * fade)
            )
            pygame.draw.circle(screen, faded_color, self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

class ParticleSystem:
    @staticmethod
    def create_explosion(x, y, color="white", particle_count=20):
        """Create an explosion effect at the given position"""
        particles = []
        for _ in range(particle_count):
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 200)
            velocity = pygame.Vector2(0, 1).rotate(angle) * speed
            particle = Particle(x, y, velocity, color, random.uniform(0.5, 1.5))
            particles.append(particle)
        return particles
