import pygame

class Tutorial:
    def __init__(self):
        self.active = False
        self.step = 0
        self.steps = [
            {"text": "Welcome to Asteroids! Press W to move forward", "condition": "move"},
            {"text": "Use A and D to rotate left and right", "condition": "rotate"},
            {"text": "Press K to shoot asteroids", "condition": "shoot"},
            {"text": "Destroy asteroids to earn points!", "condition": "destroy"},
            {"text": "Avoid collisions to stay alive. Good luck!", "condition": "complete"}
        ]
        self.completed_conditions = set()
    
    def start(self):
        """Start the tutorial"""
        self.active = True
        self.step = 0
        self.completed_conditions.clear()
    
    def mark_condition(self, condition):
        """Mark a condition as completed"""
        if condition not in self.completed_conditions:
            self.completed_conditions.add(condition)
            if condition == self.steps[self.step]["condition"]:
                self.step += 1
                if self.step >= len(self.steps):
                    self.complete()
    
    def complete(self):
        """Complete the tutorial"""
        self.active = False
    
    def get_current_text(self):
        """Get current tutorial text"""
        if self.active and self.step < len(self.steps):
            return self.steps[self.step]["text"]
        return ""
    
    def draw(self, screen):
        """Draw tutorial overlay"""
        if not self.active:
            return
        
        text = self.get_current_text()
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, "yellow")
        text_rect = text_surface.get_rect(center=(640, 100))
        
        # Draw semi-transparent background
        bg_rect = text_rect.inflate(20, 10)
        s = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        s.fill((0, 0, 0, 180))
        screen.blit(s, bg_rect.topleft)
        screen.blit(text_surface, text_rect)
