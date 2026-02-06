import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from dj import Dj

def main():
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    # Main game loop - keeps running until window is closed
    running = True
    while running:
        # Start a new game
        running = play_game(screen, game_clock)

def play_game(screen, game_clock):
    """Play a single game session. Returns True to continue, False to quit."""
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
    game_over = False

    dt = 0
    lives = 5
    invulnerable_timer = 0  # Temporary invulnerability after being hit
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit the entire game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        return True  # Restart the game
                    else:
                        paused = not paused

        if game_over:
            # Show game over screen
            screen.fill("black")
            print_game_over(screen, player, lives)
            pygame.display.flip()
            dt = game_clock.tick(60) / 1000
            continue

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
                        game_over = True
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

        print_player_score(screen, player.score)
        
        if paused:
            print_pause(screen)

        # Draw lives
        print_lives(screen, lives)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

def print_game_over(screen, player, lives):
    font_large = pygame.font.Font(None, 74)
    font_medium = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 36)
    
    # Game Over title
    text = font_large.render('GAME OVER', False, 'red')
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
    screen.blit(text, text_rect)
    
    # Final Score
    score_text = font_medium.render(f'Final Score: {player.score}', False, 'green')
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(score_text, score_rect)
    
    # Restart instruction
    restart_text = font_small.render('Press SPACE to Restart', False, 'yellow')
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80))
    screen.blit(restart_text, restart_rect)
    
    # Quit instruction
    quit_text = font_small.render('Close window to Quit', False, 'white')
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 120))
    screen.blit(quit_text, quit_rect)

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

def print_player_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', False, 'green')
    score_rect = score_text.get_rect(topleft=(10, 10))
    screen.blit(score_text, score_rect)



if __name__ == "__main__":
    main()