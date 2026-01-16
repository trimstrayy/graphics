"""
Sutherland-Hodgeman Polygon Clipping Algorithm
Clips polygons against a rectangular clipping window
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the clipping window
X_MIN, Y_MIN = 100, 100
X_MAX, Y_MAX = 500, 400

def inside(p, edge):
    """Check if point p is inside the clipping boundary for given edge"""
    x, y = p
    if edge == 'left':
        return x >= X_MIN
    elif edge == 'right':
        return x <= X_MAX
    elif edge == 'bottom':
        return y >= Y_MIN
    elif edge == 'top':
        return y <= Y_MAX

def compute_intersection(p1, p2, edge):
    """Compute intersection point of line segment p1p2 with the clipping boundary"""
    x1, y1 = p1
    x2, y2 = p2

    if edge == 'left':
        x = X_MIN
        y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
    elif edge == 'right':
        x = X_MAX
        y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
    elif edge == 'bottom':
        y = Y_MIN
        x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
    elif edge == 'top':
        y = Y_MAX
        x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)

    return [x, y]

def clip_polygon_to_edge(polygon, edge):
    """Clip polygon against a single edge"""
    output = []

    if not polygon:
        return output

    s = polygon[-1]  # Last point

    for p in polygon:
        if inside(p, edge):
            if not inside(s, edge):
                # s outside, p inside: add intersection
                output.append(compute_intersection(s, p, edge))
            output.append(p)
        elif inside(s, edge):
            # s inside, p outside: add intersection
            output.append(compute_intersection(s, p, edge))
        s = p

    return output

def sutherland_hodgeman_clip(polygon):
    """Sutherland-Hodgeman polygon clipping algorithm"""
    # Clip against each edge in sequence
    edges = ['left', 'top', 'right', 'bottom']

    for edge in edges:
        polygon = clip_polygon_to_edge(polygon, edge)

    return polygon

def plot_clipping(original_polygon, clipped_polygon, title, filename):
    """Plot the original polygon, clipping window, and clipped polygon"""
    plt.figure(figsize=(8, 6))

    # Plot clipping window
    plt.plot([X_MIN, X_MAX, X_MAX, X_MIN, X_MIN],
             [Y_MIN, Y_MIN, Y_MAX, Y_MAX, Y_MIN],
             'k-', linewidth=2, label='Clipping Window')

    # Plot original polygon
    if original_polygon:
        x_orig = [p[0] for p in original_polygon] + [original_polygon[0][0]]
        y_orig = [p[1] for p in original_polygon] + [original_polygon[0][1]]
        plt.plot(x_orig, y_orig, 'r--', linewidth=2, label='Original Polygon')

    # Plot clipped polygon
    if clipped_polygon:
        x_clip = [p[0] for p in clipped_polygon] + [clipped_polygon[0][0]]
        y_clip = [p[1] for p in clipped_polygon] + [clipped_polygon[0][1]]
        plt.plot(x_clip, y_clip, 'b-', linewidth=3, label='Clipped Polygon')
        plt.fill(x_clip, y_clip, 'b', alpha=0.3)

    plt.xlim(0, 600)
    plt.ylim(0, 500)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.savefig(f'plots/clipping/{filename}.png', dpi=150, bbox_inches='tight')
    plt.close()

# Example usage
if __name__ == "__main__":
    # Test polygons
    test_polygons = [
        # Triangle partially outside
        [[50, 150], [300, 50], [550, 200]],
        # Rectangle crossing boundaries
        [[50, 150], [550, 150], [550, 350], [50, 350]],
        # Star shape
        [[300, 50], [350, 150], [450, 150], [375, 200], [400, 300],
         [300, 225], [200, 300], [225, 200], [150, 150], [250, 150]],
        # Polygon completely inside
        [[200, 200], [300, 200], [300, 300], [200, 300]],
        # Polygon completely outside
        [[600, 500], [700, 500], [700, 600], [600, 600]],
    ]

    for i, polygon in enumerate(test_polygons):
        clipped = sutherland_hodgeman_clip(polygon)
        title = f"Sutherland-Hodgeman Polygon Clipping - Test Case {i+1}"
        filename = f"sutherland_hodgeman_{i+1}"
        plot_clipping(polygon, clipped, title, filename)
        print(f"Test Case {i+1}:")
        print(f"  Original vertices: {len(polygon)}")
        print(f"  Clipped vertices: {len(clipped)}")
        if clipped:
            print(f"  Clipped polygon: {clipped}")
        print()