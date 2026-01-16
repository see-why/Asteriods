import pygame
import random

class ScreenShake:
    def __init__(self):
        self.shake_duration = 0
        self.shake_intensity = 0
        self.offset_x = 0
        self.offset_y = 0
    
    def add_shake(self, duration=0.3, intensity=10):
        """Add screen shake effect"""
        self.shake_duration = max(self.shake_duration, duration)
        self.shake_intensity = max(self.shake_intensity, intensity)
    
    def update(self, dt):
        """Update screen shake"""
        if self.shake_duration > 0:
            self.shake_duration -= dt
            self.offset_x = random.uniform(-self.shake_intensity, self.shake_intensity)
            self.offset_y = random.uniform(-self.shake_intensity, self.shake_intensity)
        else:
            self.offset_x = 0
            self.offset_y = 0
    
    def get_offset(self):
        """Get current shake offset"""
        return (int(self.offset_x), int(self.offset_y))
