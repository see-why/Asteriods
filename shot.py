import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        end_pos = self.position + self.velocity.normalize() * (self.radius * 2)
        pygame.draw.line(screen, "white", self.position, end_pos, 2)

    def update(self, dt):
       self.position += self.velocity * dt
