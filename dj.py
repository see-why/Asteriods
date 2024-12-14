import pygame

class Dj:
    pygame.mixer.init() 
    shoot_mixer = pygame.mixer.Sound('sounds/shoot.ogg')
    asteroid_explosion_mixer = pygame.mixer.Sound("sounds/player_explodes.ogg")
    player_explosion_mixer = pygame.mixer.Sound("sounds/asteroid_explodes.wav")