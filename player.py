import pygame

from dj import Dj
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.score = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, color="white"):
        pygame.draw.polygon(screen, color, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        # k key press, K in Kill
        if keys[pygame.K_k]:
            self.rate_limit_shot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rate_limit_shot(self, dt):
        self.shoot_timer -= dt
        if self.shoot_timer > 0:
            return
        self.shoot()
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        Dj.shoot_mixer.play()

    def reset_position(self):
        self.position.x = SCREEN_WIDTH / 2
        self.position.y = SCREEN_HEIGHT / 2
        self.velocity.x = 0
        self.velocity.y = 0