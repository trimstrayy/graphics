"""
2D Scaling using OpenGL
Demonstrates scaling transformation on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [150.0, 150.0],
    [250.0, 150.0],
    [200.0, 250.0]
]

# Rectangle vertices (original)
rectangle = [
    [400.0, 150.0],
    [500.0, 150.0],
    [500.0, 250.0],
    [400.0, 250.0]
]

# Scaling parameters
sx, sy = 1.5, 0.8

def init():
    """Initialize OpenGL settings"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glColor3f(1.0, 1.0, 1.0)  # White color for drawing
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

def draw_triangle(vertices, color=(1.0, 0.0, 0.0)):
    """Draw a triangle with given vertices"""
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    # Draw outline
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def draw_rectangle(vertices, color=(0.0, 1.0, 0.0)):
    """Draw a rectangle with given vertices"""
    glColor3f(*color)
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    # Draw outline
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def scale_point(point, sx, sy, center=(WIDTH/2, HEIGHT/2)):
    """Scale a point relative to a center"""
    # Translate to origin
    x = point[0] - center[0]
    y = point[1] - center[1]

    # Scale
    x_scaled = x * sx
    y_scaled = y * sy

    # Translate back
    return [x_scaled + center[0], y_scaled + center[1]]

def scale_shape(shape, sx, sy, center=(WIDTH/2, HEIGHT/2)):
    """Scale all points in a shape relative to a center"""
    return [scale_point(point, sx, sy, center) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw scaled shapes
    scaled_triangle = scale_shape(triangle, sx, sy)
    scaled_rectangle = scale_shape(rectangle, sx, sy)

    draw_triangle(scaled_triangle, (0.0, 0.0, 1.0))  # Blue scaled triangle
    draw_rectangle(scaled_rectangle, (1.0, 1.0, 0.0))  # Yellow scaled rectangle

    # Draw scaling center
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(WIDTH/2, HEIGHT/2)
    glEnd()

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Scaling: sx={:.1f}, sy={:.1f}".format(sx, sy)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Scaled, Magenta: Center"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global sx, sy

    if key == b'w':
        sy += 0.1  # Increase Y scaling
    elif key == b's':
        sy -= 0.1  # Decrease Y scaling
    elif key == b'a':
        sx -= 0.1  # Decrease X scaling
    elif key == b'd':
        sx += 0.1  # Increase X scaling
    elif key == b'q':
        sx += 0.1  # Increase both
        sy += 0.1
    elif key == b'e':
        sx -= 0.1  # Decrease both
        sy -= 0.1
    elif key == b'r':
        sx, sy = 1.5, 0.8  # Reset
    elif key == b' ':
        sx, sy = 1.0, 1.0  # Reset to no scaling
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    # Ensure scaling factors don't go negative or too small
    sx = max(0.1, sx)
    sy = max(0.1, sy)

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Scaling - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Scaling Controls:")
    print("WASD: Adjust X/Y scaling factors")
    print("Q: Increase both scaling factors")
    print("E: Decrease both scaling factors")
    print("R: Reset to sx=1.5, sy=0.8")
    print("Space: Reset to sx=1.0, sy=1.0")
    print("ESC: Quit")
    print("Current scaling: sx={:.1f}, sy={:.1f}".format(sx, sy))

    glutMainLoop()

if __name__ == "__main__":
    main()