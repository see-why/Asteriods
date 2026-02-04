import pygame

class AudioSettings:
    def __init__(self):
        self.music_enabled = True
        self.sfx_volume = 1.0
        self.music_volume = 0.5
        self.master_volume = 1.0
    
    def toggle_music(self):
        """Toggle background music on/off"""
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            try:
                pygame.mixer.music.unpause()
            except pygame.error:
                # Ignore errors if mixer/music is not initialized
                pass
        else:
            try:
                pygame.mixer.music.pause()
            except pygame.error:
                # Ignore errors if mixer/music is not initialized
                pass
        return self.music_enabled
    
    def set_sfx_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)"""
        self.sfx_volume = max(0.0, min(1.0, volume))
    
    def set_music_volume(self, volume):
        """Set music volume (0.0 to 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
    
    def set_master_volume(self, volume):
        """Set master volume (0.0 to 1.0)"""
        self.master_volume = max(0.0, min(1.0, volume))
    
    def get_effective_sfx_volume(self):
        """Get effective SFX volume with master"""
        return self.sfx_volume * self.master_volume
