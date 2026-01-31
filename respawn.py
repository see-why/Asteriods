import pygame

class RespawnAnimation:
    def __init__(self):
        self.active = False
        self.timer = 0
        self.duration = 2.0  # Animation duration in seconds
        self.position = pygame.Vector2(0, 0)
    
    def start(self, x, y):
        """Start respawn animation at position"""
        self.active = True
        self.timer = 0
        self.position = pygame.Vector2(x, y)
    
    def update(self, dt):
        """Update animation"""
        if self.active:
            self.timer += dt
            if self.timer >= self.duration:
                self.active = False
    
    def draw(self, screen):
        """Draw respawn animation"""
        if not self.active:
            return
        
        # Calculate animation progress (0 to 1)
        progress = self.timer / self.duration
        
        # Expanding circle effect
        max_radius = 60
        radius = int(max_radius * progress)
        alpha = int(255 * (1 - progress))
        
        # Draw expanding circles
        if radius > 0:
            pygame.draw.circle(screen, "cyan", self.position, radius, 2)
            if radius > 20:
                pygame.draw.circle(screen, "white", self.position, radius - 20, 1)
    
    def is_active(self):
        """Check if animation is playing"""
        return self.active
