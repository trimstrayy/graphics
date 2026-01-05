import numpy as np
import matplotlib.pyplot as plt
import os
from transformations import Transform2D, Rectangle, Triangle, Line

def demonstrate_transformations():
    """
    Demonstrate all 2D transformations using different shapes
    """
    print("2D Transformations Demonstration")
    print("=" * 40)
    
    # Create plots directory if it doesn't exist
    os.makedirs('plots', exist_ok=True)
    
    # Create different shapes
    rectangle = Rectangle(1, 1, 3, 2)  # Rectangle at (1,1) with width 3, height 2
    triangle = Triangle((0, 0), (2, 0), (1, 2))  # Triangle with vertices
    line = Line((0, 0), (3, 2))  # Line from (0,0) to (3,2)
    
    shapes = [rectangle, triangle, line]
    
    # 1. TRANSLATION
    print("\n1. TRANSLATION")
    print("-" * 15)
    
    # Reset shapes to original
    for shape in shapes:
        shape.reset()
    
    # Apply translation (move by 2 units in x, 1 unit in y)
    for shape in shapes:
        shape.translate(2, 1)
    
    plot_shapes(shapes, "Translation (tx=2, ty=1)", "plots/translation.png")
    
    # 2. ROTATION
    print("\n2. ROTATION")
    print("-" * 10)
    
    # Reset shapes
    for shape in shapes:
        shape.reset()
    
    # Apply rotation (45 degrees)
    for shape in shapes:
        shape.rotate(45)
    
    plot_shapes(shapes, "Rotation (45 degrees)", "plots/rotation.png")
    
    # 3. SCALING
    print("\n3. SCALING")
    print("-" * 9)
    
    # Reset shapes
    for shape in shapes:
        shape.reset()
    
    # Apply scaling (scale x by 1.5, y by 0.8)
    for shape in shapes:
        shape.scale(1.5, 0.8)
    
    plot_shapes(shapes, "Scaling (sx=1.5, sy=0.8)", "plots/scaling.png")
    
    # 4. REFLECTION
    print("\n4. REFLECTION")
    print("-" * 12)
    
    # Reset shapes
    for shape in shapes:
        shape.reset()
    
    # Apply reflection across x-axis
    for shape in shapes:
        shape.reflect_x()
    
    plot_shapes(shapes, "Reflection across X-axis", "plots/reflection_x.png")
    
    # Reset and reflect across y-axis
    for shape in shapes:
        shape.reset()
        shape.reflect_y()
    
    plot_shapes(shapes, "Reflection across Y-axis", "plots/reflection_y.png")
    
    # Reset and reflect through origin
    for shape in shapes:
        shape.reset()
        shape.reflect_origin()
    
    plot_shapes(shapes, "Reflection through Origin", "plots/reflection_origin.png")
    
    # 5. SHEARING
    print("\n5. SHEARING")
    print("-" * 10)
    
    # Reset shapes
    for shape in shapes:
        shape.reset()
    
    # Apply shearing in x direction
    for shape in shapes:
        shape.shear_x(0.5)
    
    plot_shapes(shapes, "Shearing in X direction (shear_factor=0.5)", "plots/shearing_x.png")
    
    # Reset and shear in y direction
    for shape in shapes:
        shape.reset()
        shape.shear_y(0.3)
    
    plot_shapes(shapes, "Shearing in Y direction (shear_factor=0.3)", "plots/shearing_y.png")
    
    # 6. COMPOSITE TRANSFORMATIONS
    print("\n6. COMPOSITE TRANSFORMATIONS")
    print("-" * 25)
    
    # Reset shapes
    for shape in shapes:
        shape.reset()
    
    # Composite 1: Translation + Rotation
    print("Composite 1: Translation (2,1) + Rotation (30°)")
    for shape in shapes:
        shape.translate(2, 1)
        shape.rotate(30)
    
    plot_shapes(shapes, "Composite 1: Translation + Rotation", "plots/composite_1.png")
    
    # Reset and apply Composite 2: Scaling + Reflection
    for shape in shapes:
        shape.reset()
        shape.scale(1.2, 0.8)
        shape.reflect_x()
    
    plot_shapes(shapes, "Composite 2: Scaling + Reflection (X-axis)", "plots/composite_2.png")
    
    # Reset and apply Composite 3: Rotation + Shearing
    for shape in shapes:
        shape.reset()
        shape.rotate(60)
        shape.shear_x(0.4)
    
    plot_shapes(shapes, "Composite 3: Rotation + Shearing", "plots/composite_3.png")
    
    # Reset and apply Composite 4: Translation + Scaling + Rotation
    for shape in shapes:
        shape.reset()
        shape.translate(1, 1)
        shape.scale(0.8, 1.3)
        shape.rotate(-45)
    
    plot_shapes(shapes, "Composite 4: Translation + Scaling + Rotation", "plots/composite_4.png")
    
    # Reset and apply Composite 5: All transformations
    for shape in shapes:
        shape.reset()
        shape.translate(2, 0)
        shape.rotate(90)
        shape.scale(1.5, 0.7)
        shape.shear_y(0.2)
        shape.reflect_y()
    
    plot_shapes(shapes, "Composite 5: Translation + Rotation + Scaling + Shearing + Reflection", "plots/composite_5.png")

def plot_shapes(shapes_list, title="2D Transformations", save_path=None):
    """
    Plot shapes with matplotlib
    
    Args:
        shapes_list: list of Shape2D objects
        title: title for the plot
        save_path: if provided, save plot to file instead of showing
    """
    plt.figure(figsize=(10, 8))
    
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    
    for i, shape in enumerate(shapes_list):
        color = colors[i % len(colors)]
        
        if len(shape.current_vertices) == 2:
            # Line
            plt.plot(shape.current_vertices[:, 0], 
                    shape.current_vertices[:, 1], 
                    'o-', linewidth=3, markersize=10,
                    label=shape.name, color=color)
        else:
            # Polygon (close the shape for plotting)
            vertices = np.vstack([shape.current_vertices, shape.current_vertices[0]])
            plt.plot(vertices[:, 0], vertices[:, 1], 'o-', linewidth=3, markersize=10,
                    label=shape.name, color=color)
            plt.fill(vertices[:, 0], vertices[:, 1], alpha=0.3, color=color)
    
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend(loc='best', fontsize=12)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    
    # Add coordinate system
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved to: {save_path}")
    else:
        plt.show()

def demonstrate_matrix_operations():
    """
    Demonstrate matrix operations and composite transformations
    """
    print("\n\nMATRIX OPERATIONS DEMONSTRATION")
    print("=" * 35)
    
    # Create sample vertices
    vertices = np.array([[1, 1], [3, 1], [3, 3], [1, 3]], dtype=float)
    print(f"Original vertices:\n{vertices}")
    
    # Individual transformations
    T = Transform2D.translation(2, 1)
    R = Transform2D.rotation(45)
    S = Transform2D.scaling(1.5, 0.8)
    
    print(f"\nTranslation matrix (tx=2, ty=1):\n{T}")
    print(f"\nRotation matrix (45°):\n{R}")
    print(f"\nScaling matrix (sx=1.5, sy=0.8):\n{S}")
    
    # Apply individual transformations
    translated = Transform2D.apply_transformation(vertices, T)
    rotated = Transform2D.apply_transformation(vertices, R)
    scaled = Transform2D.apply_transformation(vertices, S)
    
    print(f"\nAfter translation:\n{translated}")
    print(f"\nAfter rotation:\n{rotated}")
    print(f"\nAfter scaling:\n{scaled}")
    
    # Composite transformation
    composite = Transform2D.composite_transformation(T, R, S)
    print(f"\nComposite matrix (T * R * S):\n{composite}")
    
    composite_result = Transform2D.apply_transformation(vertices, composite)
    print(f"\nAfter composite transformation:\n{composite_result}")
    
    # Verify order matters
    different_order = Transform2D.composite_transformation(R, T, S)
    different_result = Transform2D.apply_transformation(vertices, different_order)
    print(f"\nDifferent order (R * T * S):\n{different_result}")
    
    print("\nNote: Matrix multiplication is not commutative!")
    print("Order of transformations affects the final result.")

if __name__ == "__main__":
    # Run the demonstrations
    demonstrate_transformations()
    demonstrate_matrix_operations()
    
    print("\n" + "="*50)
    print("DEMONSTRATION COMPLETE")
    print("All 2D transformations have been implemented using")
    print("homogeneous coordinate systems as required.")
    print("="*50)