"""
Composite 2D Transformations using OpenGL
Demonstrates multiple transformations combined on geometric shapes
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
    [100.0, 150.0],
    [150.0, 150.0],
    [125.0, 200.0]
]

# Rectangle vertices (original)
rectangle = [
    [300.0, 150.0],
    [350.0, 150.0],
    [350.0, 200.0],
    [300.0, 200.0]
]

# Transformation parameters
tx, ty = 50.0, 30.0  # Translation
angle = 30.0  # Rotation
sx, sy = 1.2, 0.8  # Scaling
shx, shy = 0.2, 0.1  # Shearing

# Current composite mode
composite_mode = 0  # 0-4 for different combinations

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

def apply_composite_transform(shape, mode):
    """Apply composite transformation based on mode"""
    result = shape.copy()

    if mode == 0:  # Translation + Rotation
        # First translate, then rotate
        result = translate_shape(result, tx, ty)
        result = rotate_shape(result, angle)

    elif mode == 1:  # Scaling + Reflection (X-axis)
        # First scale, then reflect
        result = scale_shape(result, sx, sy)
        result = reflect_shape_x(result)

    elif mode == 2:  # Rotation + Shearing
        # First rotate, then shear
        result = rotate_shape(result, angle)
        result = shear_shape_x(result, shx)

    elif mode == 3:  # Translation + Scaling + Rotation
        # Translate, then scale, then rotate
        result = translate_shape(result, tx, ty)
        result = scale_shape(result, sx, sy)
        result = rotate_shape(result, angle)

    elif mode == 4:  # All transformations
        # Apply all transformations in sequence
        result = translate_shape(result, tx, ty)
        result = rotate_shape(result, angle)
        result = scale_shape(result, sx, sy)
        result = shear_shape_x(result, shx)
        result = reflect_shape_x(result)

    return result

# Helper transformation functions
def translate_shape(shape, tx, ty):
    return [[p[0] + tx, p[1] + ty] for p in shape]

def rotate_shape(shape, angle_deg, center=(WIDTH/2, HEIGHT/2)):
    angle_rad = math.radians(angle_deg)
    cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
    return [[center[0] + (p[0] - center[0]) * cos_a - (p[1] - center[1]) * sin_a,
             center[1] + (p[0] - center[0]) * sin_a + (p[1] - center[1]) * cos_a]
            for p in shape]

def scale_shape(shape, sx, sy, center=(WIDTH/2, HEIGHT/2)):
    return [[center[0] + (p[0] - center[0]) * sx,
             center[1] + (p[1] - center[1]) * sy]
            for p in shape]

def reflect_shape_x(shape):
    return [[p[0], HEIGHT - p[1]] for p in shape]

def shear_shape_x(shape, shx):
    return [[p[0] + shx * p[1], p[1]] for p in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw transformed shapes
    transformed_triangle = apply_composite_transform(triangle, composite_mode)
    transformed_rectangle = apply_composite_transform(rectangle, composite_mode)

    draw_triangle(transformed_triangle, (0.0, 0.0, 1.0))  # Blue transformed triangle
    draw_rectangle(transformed_rectangle, (1.0, 1.0, 0.0))  # Yellow transformed rectangle

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    mode_names = [
        "Translation + Rotation",
        "Scaling + Reflection",
        "Rotation + Shearing",
        "Translation + Scaling + Rotation",
        "All Transformations"
    ]

    glRasterPos2f(50, HEIGHT - 50)
    text = "Composite Transformations: {}".format(mode_names[composite_mode])
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Transformed"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glRasterPos2f(50, HEIGHT - 110)
    text = "Press 1-5 to change composite mode"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global composite_mode

    if key == b'1':
        composite_mode = 0
    elif key == b'2':
        composite_mode = 1
    elif key == b'3':
        composite_mode = 2
    elif key == b'4':
        composite_mode = 3
    elif key == b'5':
        composite_mode = 4
    elif key == b'r' or key == b'R':
        composite_mode = 0  # Reset
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Composite 2D Transformations - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("Composite 2D Transformations:")
    print("1: Translation + Rotation")
    print("2: Scaling + Reflection")
    print("3: Rotation + Shearing")
    print("4: Translation + Scaling + Rotation")
    print("5: All Transformations Combined")
    print("R: Reset to mode 1")
    print("ESC: Quit")
    print("Current mode: Translation + Rotation")

    glutMainLoop()

if __name__ == "__main__":
    main()