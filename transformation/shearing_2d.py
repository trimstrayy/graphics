"""
2D Shearing using OpenGL
Demonstrates shearing transformations on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [150.0, 200.0],
    [250.0, 200.0],
    [200.0, 300.0]
]

# Rectangle vertices (original)
rectangle = [
    [400.0, 200.0],
    [500.0, 200.0],
    [500.0, 300.0],
    [400.0, 300.0]
]

# Shearing parameters
shx, shy = 0.3, 0.2  # Shearing factors

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

def shear_point_x(point, shx):
    """Shear point in X direction"""
    x, y = point
    return [x + shx * y, y]

def shear_point_y(point, shy):
    """Shear point in Y direction"""
    x, y = point
    return [x, y + shy * x]

def shear_shape_x(shape, shx):
    """Shear all points in a shape in X direction"""
    return [shear_point_x(point, shx) for point in shape]

def shear_shape_y(shape, shy):
    """Shear all points in a shape in Y direction"""
    return [shear_point_y(point, shy) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw sheared shapes (X-direction)
    sheared_x_triangle = shear_shape_x(triangle, shx)
    sheared_x_rectangle = shear_shape_x(rectangle, shx)

    draw_triangle(sheared_x_triangle, (0.0, 0.0, 1.0))  # Blue X-sheared triangle
    draw_rectangle(sheared_x_rectangle, (1.0, 1.0, 0.0))  # Yellow X-sheared rectangle

    # Draw sheared shapes (Y-direction) - offset for visibility
    offset_triangle = [[p[0] + 150, p[1]] for p in triangle]
    offset_rectangle = [[p[0] + 150, p[1]] for p in rectangle]

    sheared_y_triangle = shear_shape_y(offset_triangle, shy)
    sheared_y_rectangle = shear_shape_y(offset_rectangle, shy)

    draw_triangle(sheared_y_triangle, (1.0, 0.0, 1.0))  # Magenta Y-sheared triangle
    draw_rectangle(sheared_y_rectangle, (0.0, 1.0, 1.0))  # Cyan Y-sheared rectangle

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Shearing: X-shearing={:.1f}, Y-shearing={:.1f}".format(shx, shy)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: X-sheared, Magenta/Cyan: Y-sheared"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global shx, shy

    if key == b'w':
        shy += 0.1  # Increase Y shearing
    elif key == b's':
        shy -= 0.1  # Decrease Y shearing
    elif key == b'a':
        shx -= 0.1  # Decrease X shearing
    elif key == b'd':
        shx += 0.1  # Increase X shearing
    elif key == b'q':
        shx = 0.0  # Reset X shearing
    elif key == b'e':
        shy = 0.0  # Reset Y shearing
    elif key == b'r':
        shx, shy = 0.3, 0.2  # Reset both
    elif key == b' ':
        shx, shy = 0.0, 0.0  # Reset to no shearing
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Shearing - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Shearing Controls:")
    print("WASD: Adjust shearing factors")
    print("Q: Reset X-shearing to 0")
    print("E: Reset Y-shearing to 0")
    print("R: Reset to shx=0.3, shy=0.2")
    print("Space: Reset to no shearing")
    print("ESC: Quit")
    print("Current shearing: shx={:.1f}, shy={:.1f}".format(shx, shy))

    glutMainLoop()

if __name__ == "__main__":
    main()