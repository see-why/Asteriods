import json
import os

class HighScoreManager:
    def __init__(self, filename="highscores.json"):
        self.filename = filename
        self.high_scores = self.load_high_scores()
    
    def load_high_scores(self):
        """Load high scores from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_high_scores(self):
        """Save high scores to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.high_scores, f, indent=2)
    
    def add_score(self, score, name="Player"):
        """Add a new score to the high scores list"""
        self.high_scores.append({
            "name": name,
            "score": score
        })
        # Sort by score (highest first) and keep top 10
        self.high_scores.sort(key=lambda x: x["score"], reverse=True)
        self.high_scores = self.high_scores[:10]
        self.save_high_scores()
    
    def is_high_score(self, score):
        """Check if a score qualifies as a high score"""
        if len(self.high_scores) < 10:
            return True
        return score > self.high_scores[-1]["score"]
    
    def get_high_scores(self):
        """Get the list of high scores"""
        return self.high_scores
