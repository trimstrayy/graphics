from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Implement Mid-point Circle Drawing Algorithm
def midpoint_circle(xc, yc, r):
    glBegin(GL_POINTS)
    x = 0
    y = r
    p = 1 - r
    plot_circle_points(xc, yc, x, y)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
        plot_circle_points(xc, yc, x, y)
    glEnd()

def plot_circle_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Draw a circle at (325,200) with radius 100
    midpoint_circle(325, 200, 100)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"Midpoint Circle - OpenGL")
init()
glutDisplayFunc(display)
glutMainLoop()