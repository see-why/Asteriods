import pygame

class Dj:
    pygame.mixer.init() 
    shoot_mixer = pygame.mixer.Sound('sounds/shoot.ogg')
    shoot_mixer.set_volume(0.1)
    player_explosion_mixer = pygame.mixer.Sound("sounds/player_explodes.ogg")
    player_explosion_mixer.set_volume(0.1)
    asteroid_explosion_mixer = pygame.mixer.Sound("sounds/asteroid_explodes.wav")
    asteroid_explosion_mixer.set_volume(0.1)