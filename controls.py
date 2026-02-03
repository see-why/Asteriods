import json
import os

class ControlSettings:
    def __init__(self):
        self.controls_file = "controls.json"
        self.default_controls = {
            "rotate_left": "a",
            "rotate_right": "d",
            "move_forward": "w",
            "move_backward": "z",
            "shoot": "k",
            "pause": "space"
        }
        self.controls = self.load_controls()
    
    def load_controls(self):
        """Load control settings from file"""
        if os.path.exists(self.controls_file):
            try:
                with open(self.controls_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Failed to load controls: {e}")
                return self.default_controls.copy()
        return self.default_controls.copy()
    
    def save_controls(self):
        """Save control settings to file"""
        with open(self.controls_file, 'w') as f:
            json.dump(self.controls, f, indent=2)
    
    def set_control(self, action, key):
        """Set a control binding"""
        if action in self.controls:
            self.controls[action] = key
            self.save_controls()
    
    def get_control(self, action):
        """Get control key for an action"""
        return self.controls.get(action, self.default_controls.get(action))
    
    def reset_to_defaults(self):
        """Reset all controls to defaults"""
        self.controls = self.default_controls.copy()
        self.save_controls()
