import time

class TimeAttackMode:
    def __init__(self, duration=120):
        self.duration = duration  # Time limit in seconds
        self.time_remaining = duration
        self.active = False
        self.final_score = 0
        self.leaderboard = []
    
    def start(self):
        """Start time attack mode"""
        self.active = True
        self.time_remaining = self.duration
        self.final_score = 0
    
    def update(self, dt):
        """Update timer"""
        if self.active:
            self.time_remaining -= dt
            if self.time_remaining <= 0:
                self.time_remaining = 0
                self.finish()
    
    def finish(self):
        """End time attack mode"""
        self.active = False
    
    def is_finished(self):
        """Check if time is up"""
        return self.time_remaining <= 0
    
    def get_time_remaining(self):
        """Get formatted time remaining"""
        minutes = int(self.time_remaining // 60)
        seconds = int(self.time_remaining % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def add_to_leaderboard(self, score, name="Player"):
        """Add score to leaderboard"""
        self.leaderboard.append({"name": name, "score": score})
        self.leaderboard.sort(key=lambda x: x["score"], reverse=True)
        self.leaderboard = self.leaderboard[:10]
    
    def get_leaderboard(self):
        """Get top scores"""
        return self.leaderboard
