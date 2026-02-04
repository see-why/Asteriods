import pygame

class PerformanceOptimizer:
    """Optimizations for rendering and collision detection"""
    
    def __init__(self):
        self.spatial_grid = {}
        self.grid_size = 100
    
    def build_spatial_grid(self, objects):
        """Build spatial hash grid for faster collision detection"""
        self.spatial_grid.clear()
        
        for obj in objects:
            grid_x = int(obj.position.x // self.grid_size)
            grid_y = int(obj.position.y // self.grid_size)
            
            key = (grid_x, grid_y)
            if key not in self.spatial_grid:
                self.spatial_grid[key] = []
            self.spatial_grid[key].append(obj)
    
    def get_nearby_objects(self, obj):
        """Get objects in nearby grid cells"""
        grid_x = int(obj.position.x // self.grid_size)
        grid_y = int(obj.position.y // self.grid_size)
        
        nearby = []
        # Check surrounding cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                key = (grid_x + dx, grid_y + dy)
                if key in self.spatial_grid:
                    nearby.extend(self.spatial_grid[key])
        
        return nearby
    
    @staticmethod
    def cull_offscreen(objects, screen_width, screen_height, margin=200):
        """Remove objects far outside screen bounds by calling kill() on sprites"""
        for obj in objects[:]:  # Iterate over a copy to safely modify during iteration
            if not (-margin < obj.position.x < screen_width + margin and
                    -margin < obj.position.y < screen_height + margin):
                # Call kill() to remove sprite from all its sprite groups
                if hasattr(obj, 'kill'):
                    obj.kill()
    
    @staticmethod
    def optimize_draw_calls(sprites):
        """Batch similar draw operations"""
        # Group sprites by type for batch rendering
        batched = {}
        for sprite in sprites:
            sprite_type = type(sprite).__name__
            if sprite_type not in batched:
                batched[sprite_type] = []
            batched[sprite_type].append(sprite)
        return batched
