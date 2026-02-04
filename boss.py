import pygame
from asteroid import Asteroid
from constants import ASTEROID_MAX_RADIUS

class BossAsteroid(Asteroid):
    def __init__(self, x, y):
        super().__init__(x, y, ASTEROID_MAX_RADIUS * 2)
        self.health = 10
        self.max_health = 10
        self.asteroid_type = "boss"
        self.color = "purple"
    
    def draw(self, screen):
        # Draw boss asteroid with special appearance
        pygame.draw.circle(screen, self.color, self.position, self.radius, 3)
        # Draw inner circle
        pygame.draw.circle(screen, "yellow", self.position, self.radius * 0.7, 2)
        
        # Draw health bar
        health_bar_width = self.radius * 2
        health_bar_height = 5
        if self.max_health > 0:
            health_percent = self.health / self.max_health
        else:
            health_percent = 0.0
        
        bar_x = self.position.x - health_bar_width / 2
        bar_y = self.position.y - self.radius - 15
        
        # Background bar
        pygame.draw.rect(screen, "red", (bar_x, bar_y, health_bar_width, health_bar_height))
        # Health bar
        pygame.draw.rect(screen, "green", (bar_x, bar_y, health_bar_width * health_percent, health_bar_height))
    
    def take_damage(self):
        """Reduce health when hit"""
        self.health -= 1
        return self.health <= 0
    
    def split(self):
        """Boss splits into multiple large asteroids"""
        if self.health > 0:
            return  # Boss doesn't split until destroyed
        
        self.kill()
        
        # Spawn 4 large asteroids
        for i in range(4):
            angle = i * 90
            velocity = pygame.Vector2(0, 1).rotate(angle) * 80
            asteroid = Asteroid(self.position.x, self.position.y, ASTEROID_MAX_RADIUS)
            asteroid.velocity = velocity
            
            # Ensure the new asteroid is added to any configured sprite groups
            containers = getattr(Asteroid, "containers", None)
            if containers:
                asteroid.add(*containers)
