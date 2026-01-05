from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Implement Bresenham Line Drawing algorithm for both slopes (|m|<1 and |m|>=1)
def bresenham_line(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        glVertex2f(x1, y1)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Draw a line with slope < 1
    bresenham_line(50, 50, 600, 150)
    # Draw a line with slope >= 1
    bresenham_line(50, 50, 150, 350)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"Bresenham Line - OpenGL")
init()
glutDisplayFunc(display)
glutMainLoop()