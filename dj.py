import pygame

# Try to initialize mixer, but handle gracefully if not available
try:
    pygame.mixer.init()
    MIXER_AVAILABLE = True
except (NotImplementedError, ModuleNotFoundError):
    MIXER_AVAILABLE = False
    print("Warning: pygame.mixer not available - audio will be disabled")

class Dj:
    if MIXER_AVAILABLE:
        shoot_mixer = pygame.mixer.Sound('sounds/shoot.ogg')
        shoot_mixer.set_volume(0.1)
        player_explosion_mixer = pygame.mixer.Sound("sounds/player_explodes.ogg")
        player_explosion_mixer.set_volume(0.1)
        asteroid_explosion_mixer = pygame.mixer.Sound("sounds/asteroid_explodes.wav")
        asteroid_explosion_mixer.set_volume(0.1)
    else:
        # Create dummy objects that do nothing when mixer is unavailable
        class DummySound:
            def play(self): pass
            def set_volume(self, vol): pass
        
        shoot_mixer = DummySound()
        player_explosion_mixer = DummySound()
        asteroid_explosion_mixer = DummySound()