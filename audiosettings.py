import pygame

class AudioSettings:
    def __init__(self):
        self.music_enabled = True
        self.sfx_volume = 1.0
        self.music_volume = 0.5
    
    def toggle_music(self):
        """Toggle background music on/off"""
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            # Resume music
            pass
        else:
            # Pause music
            pass
        return self.music_enabled
    
    def set_sfx_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)"""
        self.sfx_volume = max(0.0, min(1.0, volume))
    
    def set_music_volume(self, volume):
        """Set music volume (0.0 to 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
