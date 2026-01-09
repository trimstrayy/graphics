"""
2D Rotation using OpenGL
Demonstrates rotation transformation on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [200.0, 200.0],
    [300.0, 200.0],
    [250.0, 300.0]
]

# Rectangle vertices (original)
rectangle = [
    [450.0, 150.0],
    [550.0, 150.0],
    [550.0, 250.0],
    [450.0, 250.0]
]

# Rotation parameters
angle = 30.0  # degrees
rotation_speed = 2.0

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

def rotate_point(point, angle_degrees, center=(WIDTH/2, HEIGHT/2)):
    """Rotate a point around a center point"""
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)

    # Translate to origin
    x = point[0] - center[0]
    y = point[1] - center[1]

    # Rotate
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a

    # Translate back
    return [x_new + center[0], y_new + center[1]]

def rotate_shape(shape, angle, center=(WIDTH/2, HEIGHT/2)):
    """Rotate all points in a shape around a center"""
    return [rotate_point(point, angle, center) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw rotated shapes
    rotated_triangle = rotate_shape(triangle, angle)
    rotated_rectangle = rotate_shape(rectangle, angle)

    draw_triangle(rotated_triangle, (0.0, 0.0, 1.0))  # Blue rotated triangle
    draw_rectangle(rotated_rectangle, (1.0, 1.0, 0.0))  # Yellow rotated rectangle

    # Draw rotation center
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(WIDTH/2, HEIGHT/2)
    glEnd()

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Rotation: {:.1f} degrees".format(angle)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Rotated, Magenta: Center"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global angle

    if key == b'q':
        angle += rotation_speed  # Rotate clockwise
    elif key == b'e':
        angle -= rotation_speed  # Rotate counter-clockwise
    elif key == b'r':
        angle = 30.0  # Reset
    elif key == b' ':
        angle = 0.0  # Reset to 0
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def idle():
    """Idle callback for continuous rotation"""
    global angle
    angle += 0.5  # Slow continuous rotation
    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Rotation - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    # glutIdleFunc(idle)  # Uncomment for continuous rotation

    print("2D Rotation Controls:")
    print("Q: Rotate clockwise")
    print("E: Rotate counter-clockwise")
    print("R: Reset to 30 degrees")
    print("Space: Reset to 0 degrees")
    print("ESC: Quit")
    print("Current angle: {:.1f} degrees".format(angle))

    glutMainLoop()

if __name__ == "__main__":
    main()