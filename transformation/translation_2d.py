"""
2D Translation using OpenGL
Demonstrates translation transformation on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [100.0, 100.0],
    [200.0, 100.0],
    [150.0, 200.0]
]

# Rectangle vertices (original)
rectangle = [
    [300.0, 100.0],
    [400.0, 100.0],
    [400.0, 200.0],
    [300.0, 200.0]
]

# Translation parameters
tx, ty = 50.0, 30.0

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

def translate_point(point, tx, ty):
    """Translate a single point"""
    return [point[0] + tx, point[1] + ty]

def translate_shape(shape, tx, ty):
    """Translate all points in a shape"""
    return [translate_point(point, tx, ty) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw translated shapes
    translated_triangle = translate_shape(triangle, tx, ty)
    translated_rectangle = translate_shape(rectangle, tx, ty)

    draw_triangle(translated_triangle, (0.0, 0.0, 1.0))  # Blue translated triangle
    draw_rectangle(translated_rectangle, (1.0, 1.0, 0.0))  # Yellow translated rectangle

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Translation: tx={}, ty={}".format(tx, ty)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original Shapes, Blue/Yellow: Translated Shapes"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global tx, ty

    if key == b'w':
        ty += 10  # Move up
    elif key == b's':
        ty -= 10  # Move down
    elif key == b'a':
        tx -= 10  # Move left
    elif key == b'd':
        tx += 10  # Move right
    elif key == b'r':
        tx, ty = 50.0, 30.0  # Reset
    elif key == b'q' or key == b'\x1b':  # ESC or q
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Translation - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Translation Controls:")
    print("WASD: Move translation vector")
    print("R: Reset to original translation")
    print("Q or ESC: Quit")
    print("Translation vector: tx={}, ty={}".format(tx, ty))

    glutMainLoop()

if __name__ == "__main__":
    main()