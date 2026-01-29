import pygame
import random

class AsteroidFragment:
    """Small debris pieces from destroyed asteroids"""
    def __init__(self, x, y, velocity, color="gray"):
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.color = color
        self.lifetime = random.uniform(0.5, 1.5)
        self.size = random.randint(1, 3)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-200, 200)
    
    def update(self, dt):
        """Update fragment position and lifetime"""
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt
        self.lifetime -= dt
        self.velocity *= 0.95  # Slow down over time
    
    def draw(self, screen):
        """Draw fragment"""
        if self.lifetime > 0:
            alpha = int(255 * (self.lifetime / 1.5))
            pygame.draw.circle(screen, self.color, self.position, self.size)
    
    def is_alive(self):
        """Check if fragment is still visible"""
        return self.lifetime > 0

class FragmentSystem:
    def __init__(self):
        self.fragments = []
    
    def create_fragments(self, x, y, color, count=10):
        """Create debris fragments at position"""
        for _ in range(count):
            angle = random.uniform(0, 360)
            speed = random.uniform(30, 100)
            velocity = pygame.Vector2(0, 1).rotate(angle) * speed
            fragment = AsteroidFragment(x, y, velocity, color)
            self.fragments.append(fragment)
    
    def update(self, dt):
        """Update all fragments"""
        self.fragments = [f for f in self.fragments if f.is_alive()]
        for fragment in self.fragments:
            fragment.update(dt)
    
    def draw(self, screen):
        """Draw all fragments"""
        for fragment in self.fragments:
            fragment.draw(screen)
