class LevelSystem:
    def __init__(self):
        self.current_level = 1
        self.asteroids_destroyed = 0
        self.asteroids_per_level = 10
    
    def add_destroyed_asteroid(self):
        """Track asteroid destruction and check for level up"""
        self.asteroids_destroyed += 1
        if self.asteroids_destroyed >= self.asteroids_per_level:
            self.level_up()
    
    def level_up(self):
        """Advance to next level"""
        self.current_level += 1
        self.asteroids_destroyed = 0
        # Increase difficulty slightly each level
        self.asteroids_per_level = int(10 + (self.current_level * 2))
    
    def get_spawn_rate_multiplier(self):
        """Get spawn rate multiplier based on level"""
        return max(0.3, 1.0 - (self.current_level * 0.05))
    
    def get_asteroid_speed_multiplier(self):
        """Get asteroid speed multiplier based on level"""
        return 1.0 + (self.current_level * 0.1)
    
    def get_progress(self):
        """Get progress towards next level as percentage"""
        if self.asteroids_per_level == 0:
            return 0
        return (self.asteroids_destroyed / self.asteroids_per_level) * 100
