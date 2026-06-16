import math

def apply_gravitational_pull(grid_space, mass_x, mass_y, mass_val):
    """Calculates vector force fields using standard inverse-square laws."""
    g_constant = 6.674
    
    for r in range(grid_space.size):
        for c in range(grid_space.size):
            if r == mass_x and c == mass_y:
                continue
            
            dx = mass_x - r
            dy = mass_y - c
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance > 0:
                force = (g_constant * mass_val) / (distance ** 2)
                # Resolve force magnitude down to standard X/Y vectors
                grid_space.matrix_grid[r][c][0] += force * (dx / distance)
                grid_space.matrix_grid[r][c][1] += force * (dy / distance)
