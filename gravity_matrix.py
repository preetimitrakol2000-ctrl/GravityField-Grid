class SpatialGravityGrid:
    def __init__(self, size=5):
        self.size = size
        # Dense Grid Layout tracking vector coordinates [Force_X, Force_Y] initialized to zero
        self.matrix_grid = [[ [0.0, 0.0] for _ in range(size)] for _ in range(size)
