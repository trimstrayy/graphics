from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Implement Digital Differential Analyzer Line drawing algorithm
def dda_line(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        glVertex2f(x1, y1)
    else:
        x_inc = dx / steps
        y_inc = dy / steps
        x = x1
        y = y1
        for _ in range(int(steps) + 1):
            glVertex2f(x, y)
            x += x_inc
            y += y_inc
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Draw a single line from (100, 100) to (500, 300)
    dda_line(100, 100, 500, 300)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"DDA Line - OpenGL")
init()
glutDisplayFunc(display)
glutMainLoop()