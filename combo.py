class ComboSystem:
    def __init__(self):
        self.combo_count = 0
        self.combo_timer = 0
        self.combo_timeout = 3.0  # seconds before combo resets
        self.combo_multiplier = 1.0
    
    def add_hit(self):
        """Register a hit and increase combo"""
        self.combo_count += 1
        self.combo_timer = self.combo_timeout
        
        # Update multiplier based on combo count
        if self.combo_count >= 10:
            self.combo_multiplier = 3.0
        elif self.combo_count >= 5:
            self.combo_multiplier = 2.0
        else:
            self.combo_multiplier = 1.0 + (self.combo_count * 0.1)
    
    def update(self, dt):
        """Update combo timer"""
        if self.combo_timer > 0:
            self.combo_timer -= dt
            if self.combo_timer <= 0:
                self.reset()
    
    def reset(self):
        """Reset combo counter"""
        self.combo_count = 0
        self.combo_multiplier = 1.0
        self.combo_timer = 0
    
    def get_bonus_points(self, base_points):
        """Calculate bonus points based on combo"""
        return int(base_points * self.combo_multiplier)
    
    def get_combo_text(self):
        """Get combo display text"""
        if self.combo_count > 1:
            return f"COMBO x{self.combo_count} ({self.combo_multiplier:.1f}x)"
        return ""
