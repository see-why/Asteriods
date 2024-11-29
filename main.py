import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    paused = False

    dt = 0
    game_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space button clicked")
                    paused = not paused

        if not paused:
            for sprite in updatable:
                sprite.update(dt)

            for asteroid in asteroids:
                if asteroid.collides(player):
                    print("Game Over")
                    sys.exit()
                
                for shot in shots:
                    if asteroid.collides(shot):
                        asteroid.split()
                        shot.kill()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)
        
        if paused:
            font = pygame.font.Font(None, 74)
            text = font.render('PAUSED', False, 'red')
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        dt = game_clock.tick(60) / 10000


if __name__ == "__main__":
    main()