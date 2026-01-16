"""
Liang-Barsky Line Clipping Algorithm
Parametric line clipping against a rectangular window
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the clipping window
X_MIN, Y_MIN = 100, 100
X_MAX, Y_MAX = 500, 400

def liang_barsky_clip(x1, y1, x2, y2):
    """Liang-Barsky line clipping algorithm"""
    dx = x2 - x1
    dy = y2 - y1

    # Parametric equations: x = x1 + dx*t, y = y1 + dy*t
    # Clipping boundaries
    p = [-dx, dx, -dy, dy]
    q = [x1 - X_MIN, X_MAX - x1, y1 - Y_MIN, Y_MAX - y1]

    t_enter = 0.0
    t_exit = 1.0

    for i in range(4):
        if p[i] == 0:
            # Parallel to boundary
            if q[i] < 0:
                # Line is outside and parallel
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                # Potentially entering
                if t > t_enter:
                    t_enter = t
            else:
                # Potentially exiting
                if t < t_exit:
                    t_exit = t

    if t_enter > t_exit:
        # No valid intersection
        return None

    # Clip the line
    x1_clip = x1 + dx * t_enter
    y1_clip = y1 + dy * t_enter
    x2_clip = x1 + dx * t_exit
    y2_clip = y1 + dy * t_exit

    return x1_clip, y1_clip, x2_clip, y2_clip

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
        clipped = liang_barsky_clip(x1, y1, x2, y2)
        title = f"Liang-Barsky Line Clipping - Test Case {i+1}"
        filename = f"liang_barsky_{i+1}"
        plot_clipping(x1, y1, x2, y2, clipped, title, filename)
        print(f"Test Case {i+1}: Original ({x1}, {y1}) to ({x2}, {y2})")
        if clipped:
            print(f"  Clipped: ({clipped[0]:.2f}, {clipped[1]:.2f}) to ({clipped[2]:.2f}, {clipped[3]:.2f})")
        else:
            print("  No intersection - line completely outside")
        print()