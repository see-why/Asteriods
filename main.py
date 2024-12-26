import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from dj import Dj

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
    lives = 5
    invulnerable_timer = 0  # Temporary invulnerability after being hit
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            # Update invulnerability timer
            if invulnerable_timer > 0:
                invulnerable_timer -= (dt * 100)
            
            for sprite in updatable:
                sprite.update(dt)

            for asteroid in asteroids:
                if asteroid.collides(player) and invulnerable_timer <= 0:
                    Dj.player_explosion_mixer.play()
                    lives -= 1
                    invulnerable_timer = 200  # 2 seconds of invulnerability
                    if lives <= 0:
                        game_over_timer = 5000
                        print_game_over(screen, player)
                        while game_over_timer > 0:
                            game_over_timer -= (dt/ 1000)
                            
                        sys.exit()
                    else:
                        player.reset_position()

                for shot in shots:
                    if asteroid.collides(shot):
                        Dj.asteroid_explosion_mixer.play()
                        asteroid.split()
                        shot.kill()
                        point = int(1000 / asteroid.radius)
                        player.score += point

        screen.fill("black")

        for sprite in drawable:
            color = None
            if sprite == player:
                if invulnerable_timer > 0:
                    # Flash red during invulnerability
                    color = "red" if int(invulnerable_timer / 4) % 2 == 0 else None
                else:
                    color = "green"
            sprite.draw(screen, color) if color else sprite.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {player.score}', False, 'green')
        score_rect = score_text.get_rect(topleft=(10, 10))
        screen.blit(score_text, score_rect)
        
        if paused:
            print_pause(screen)

        # Draw lives
        print_lives(screen, lives)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

def print_game_over(screen, player):
    screen.fill("black")
    font = pygame.font.Font(None, 74)
    text = font.render('GAME OVER', False, 'red')
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)
    
    score_text = font.render(f'Final Score: {player.score}', False, 'green')
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80))
    screen.blit(score_text, score_rect)
    pygame.display.flip()

def print_pause(screen):
    font = pygame.font.Font(None, 74)
    text = font.render('PAUSED', False, 'red')
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)

def print_lives(screen, lives):
    for i in range(lives):
        pygame.draw.polygon(screen, 'green', [
            (30 + i*30, 50),
            (45 + i*30, 70),
            (15 + i*30, 70)
        ])



if __name__ == "__main__":
    main()