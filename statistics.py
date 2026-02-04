class GameStatistics:
    def __init__(self):
        self.total_shots_fired = 0
        self.total_hits = 0
        self.total_asteroids_destroyed = 0
        self.total_damage_taken = 0
        self.max_combo = 0
        self.playtime = 0
    
    def update(self, dt):
        """Update playtime"""
        self.playtime += dt
    
    def record_shot(self):
        """Record a shot fired"""
        self.total_shots_fired += 1
    
    def record_hit(self):
        """Record a successful hit"""
        self.total_hits += 1
    
    def record_asteroid_destroyed(self):
        """Record an asteroid destruction"""
        self.total_asteroids_destroyed += 1
    
    def record_damage(self):
        """Record damage taken"""
        self.total_damage_taken += 1
    
    def update_max_combo(self, combo):
        """Update max combo achieved"""
        self.max_combo = max(self.max_combo, combo)
    
    def get_accuracy(self):
        """Calculate shooting accuracy"""
        if self.total_shots_fired == 0:
            return 0
        return (self.total_hits / self.total_shots_fired) * 100
    
    def get_stats_summary(self):
        """Get formatted statistics"""
        return {
            "playtime": int(self.playtime),
            "accuracy": f"{self.get_accuracy():.1f}%",
            "asteroids_destroyed": self.total_asteroids_destroyed,
            "max_combo": self.max_combo,
            "damage_taken": self.total_damage_taken
        }
