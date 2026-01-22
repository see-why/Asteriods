class ScoreMultiplier:
    def __init__(self):
        self.base_multiplier = 1.0
        self.time_bonus_multiplier = 1.0
        self.survival_time = 0
    
    def update(self, dt):
        """Update survival time and calculate time bonus"""
        self.survival_time += dt
        # Increase multiplier every 30 seconds
        self.time_bonus_multiplier = 1.0 + (int(self.survival_time / 30) * 0.25)
    
    def get_total_multiplier(self):
        """Get total score multiplier"""
        return self.base_multiplier * self.time_bonus_multiplier
    
    def set_base_multiplier(self, multiplier):
        """Set base multiplier (e.g., from difficulty)"""
        self.base_multiplier = multiplier
    
    def reset(self):
        """Reset multiplier on death"""
        self.survival_time = 0
        self.time_bonus_multiplier = 1.0
