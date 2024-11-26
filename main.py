import pygame

from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)


    dt = 0
    game_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 10000


if __name__ == "__main__":
    main()