class AchievementSystem:
    def __init__(self):
        self.achievements = {
            "first_blood": {"name": "First Blood", "description": "Destroy your first asteroid", "unlocked": False},
            "sharpshooter": {"name": "Sharpshooter", "description": "Reach a 10x combo", "unlocked": False},
            "survivor": {"name": "Survivor", "description": "Reach level 5", "unlocked": False},
            "ace_pilot": {"name": "Ace Pilot", "description": "Score 10,000 points", "unlocked": False},
            "untouchable": {"name": "Untouchable", "description": "Complete a level without taking damage", "unlocked": False},
            "boss_slayer": {"name": "Boss Slayer", "description": "Defeat a boss asteroid", "unlocked": False}
        }
        self.recent_unlock = None
        self.unlock_timer = 0
    
    def check_achievement(self, achievement_id):
        """Check and unlock an achievement"""
        if achievement_id in self.achievements and not self.achievements[achievement_id]["unlocked"]:
            self.achievements[achievement_id]["unlocked"] = True
            self.recent_unlock = self.achievements[achievement_id]
            self.unlock_timer = 3.0  # Show notification for 3 seconds
            return True
        return False
    
    def update(self, dt):
        """Update achievement notification timer"""
        if self.unlock_timer > 0:
            self.unlock_timer -= dt
        else:
            self.recent_unlock = None
    
    def get_unlocked_count(self):
        """Get number of unlocked achievements"""
        return sum(1 for a in self.achievements.values() if a["unlocked"])
