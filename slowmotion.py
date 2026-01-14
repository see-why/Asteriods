class SlowMotion:
    def __init__(self):
        self.active = False
        self.timer = 0
        self.slow_factor = 0.3  # Time runs at 30% speed
    
    def activate(self, duration=3.0):
        """Activate slow motion for specified duration"""
        self.active = True
        self.timer = duration
    
    def update(self, dt):
        """Update slow motion timer"""
        if self.timer > 0:
            self.timer -= dt
            self.active = True
        else:
            self.active = False
    
    def get_time_scale(self):
        """Get current time scale"""
        return self.slow_factor if self.active else 1.0
