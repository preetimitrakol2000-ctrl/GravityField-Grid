from gravity_matrix import SpatialGravityGrid
from field_physics import apply_gravitational_pull
from vector_agent import inspect_field_point

if __name__ == "__main__":
    print("🌌 Launching Dense Spatial GravityField-Grid Engine...\n")

    space_map = SpatialGravityGrid(size=4)
    
    # Position a massive object at matrix coordinates [2, 2]
    apply_gravitational_pull(space_map, mass_x=2, mass_y=2, mass_val=500.0)

    test_x, test_y = 0, 0
    force_vector = inspect_field_point(space_map, test_x, test_y)

    print(f"📥 Heavy Mass Object Positioned at Coordinates Target: [2, 2]")
    print(f"🔍 Analyzing Field Metrics at Corner Point: [{test_x}, {test_y}]")
    print(f"🔮 Calculated Acceleration Vector: Force_X = {force_vector[0]:.4f} | Force_Y = {force_vector[1]:.4f}")
