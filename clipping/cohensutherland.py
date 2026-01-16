"""
Cohen-Sutherland Line Clipping Algorithm
Clips line segments against a rectangular clipping window
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the clipping window
X_MIN, Y_MIN = 100, 100
X_MAX, Y_MAX = 500, 400

# Region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(x, y):
    """Compute the region code for a point (x, y)"""
    code = INSIDE

    if x < X_MIN:
        code |= LEFT
    elif x > X_MAX:
        code |= RIGHT

    if y < Y_MIN:
        code |= BOTTOM
    elif y > Y_MAX:
        code |= TOP

    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    """Cohen-Sutherland line clipping algorithm"""
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            # Both points inside
            accept = True
            break
        elif (code1 & code2) != 0:
            # Both points in same outside region
            break
        else:
            # Some segment is inside
            x, y = 0.0, 0.0

            # Choose the point outside the window
            code_out = code1 if code1 != 0 else code2

            # Find intersection point
            if code_out & TOP:
                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
                y = Y_MAX
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
                y = Y_MIN
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
                x = X_MAX
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
                x = X_MIN

            # Replace the outside point with intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return x1, y1, x2, y2
    else:
        return None

def plot_clipping(x1, y1, x2, y2, clipped, title, filename):
    """Plot the original line, clipping window, and clipped line"""
    plt.figure(figsize=(8, 6))

    # Plot clipping window
    plt.plot([X_MIN, X_MAX, X_MAX, X_MIN, X_MIN],
             [Y_MIN, Y_MIN, Y_MAX, Y_MAX, Y_MIN],
             'k-', linewidth=2, label='Clipping Window')

    # Plot original line
    plt.plot([x1, x2], [y1, y2], 'r--', linewidth=2, label='Original Line')

    # Plot clipped line if exists
    if clipped:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2], 'b-', linewidth=3, label='Clipped Line')

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
    # Test cases
    test_lines = [
        (50, 150, 550, 350),    # Crosses right boundary
        (150, 50, 350, 450),    # Crosses top boundary
        (50, 50, 550, 450),     # Crosses multiple boundaries
        (200, 200, 300, 300),   # Completely inside
        (600, 500, 700, 600),   # Completely outside
    ]

    for i, (x1, y1, x2, y2) in enumerate(test_lines):
        clipped = cohen_sutherland_clip(x1, y1, x2, y2)
        title = f"Cohen-Sutherland Line Clipping - Test Case {i+1}"
        filename = f"cohen_sutherland_{i+1}"
        plot_clipping(x1, y1, x2, y2, clipped, title, filename)
        print(f"Test Case {i+1}: Original ({x1}, {y1}) to ({x2}, {y2})")
        if clipped:
            print(f"  Clipped: ({clipped[0]:.2f}, {clipped[1]:.2f}) to ({clipped[2]:.2f}, {clipped[3]:.2f})")
        else:
            print("  No intersection - line completely outside")
        print()