"""
2D Reflection using OpenGL
Demonstrates reflection transformations on geometric shapes
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

# Reflection mode
reflection_mode = 0  # 0: X-axis, 1: Y-axis, 2: Origin

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

def reflect_point_x_axis(point):
    """Reflect point across X-axis"""
    return [point[0], HEIGHT - point[1]]

def reflect_point_y_axis(point):
    """Reflect point across Y-axis"""
    return [WIDTH - point[0], point[1]]

def reflect_point_origin(point):
    """Reflect point through origin"""
    return [WIDTH - point[0], HEIGHT - point[1]]

def reflect_shape(shape, mode):
    """Reflect all points in a shape"""
    if mode == 0:  # X-axis
        return [reflect_point_x_axis(point) for point in shape]
    elif mode == 1:  # Y-axis
        return [reflect_point_y_axis(point) for point in shape]
    elif mode == 2:  # Origin
        return [reflect_point_origin(point) for point in shape]
    return shape

def draw_axes():
    """Draw coordinate axes"""
    glColor3f(0.5, 0.5, 0.5)  # Gray

    # X-axis
    glBegin(GL_LINES)
    glVertex2f(0, HEIGHT/2)
    glVertex2f(WIDTH, HEIGHT/2)
    glEnd()

    # Y-axis
    glBegin(GL_LINES)
    glVertex2f(WIDTH/2, 0)
    glVertex2f(WIDTH/2, HEIGHT)
    glEnd()

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw coordinate axes
    draw_axes()

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw reflected shapes
    reflected_triangle = reflect_shape(triangle, reflection_mode)
    reflected_rectangle = reflect_shape(rectangle, reflection_mode)

    draw_triangle(reflected_triangle, (0.0, 0.0, 1.0))  # Blue reflected triangle
    draw_rectangle(reflected_rectangle, (1.0, 1.0, 0.0))  # Yellow reflected rectangle

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    mode_names = ["X-axis", "Y-axis", "Origin"]
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Reflection: {}".format(mode_names[reflection_mode])
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Reflected"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glRasterPos2f(50, HEIGHT - 110)
    text = "Press 1,2,3 to change reflection mode"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global reflection_mode

    if key == b'1':
        reflection_mode = 0  # X-axis
    elif key == b'2':
        reflection_mode = 1  # Y-axis
    elif key == b'3':
        reflection_mode = 2  # Origin
    elif key == b'r' or key == b'R':
        reflection_mode = 0  # Reset to X-axis
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Reflection - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Reflection Controls:")
    print("1: Reflect across X-axis")
    print("2: Reflect across Y-axis")
    print("3: Reflect through Origin")
    print("R: Reset to X-axis reflection")
    print("ESC: Quit")
    print("Current mode: X-axis reflection")

    glutMainLoop()

if __name__ == "__main__":
    main()