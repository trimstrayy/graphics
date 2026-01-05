from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Implement Midpoint Ellipse drawing Algorithm
def midpoint_ellipse(xc, yc, rx, ry):
    glBegin(GL_POINTS)
    x = 0
    y = ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        x += 1
        dx += 2 * ry**2
        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy -= 2 * rx**2
            p1 += dx - dy + ry**2
    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        y -= 1
        dy -= 2 * rx**2
        if p2 > 0:
            p2 += rx**2 - dy
        else:
            x += 1
            dx += 2 * ry**2
            p2 += dx - dy + rx**2
    glEnd()

def plot_ellipse_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Draw an ellipse at (325,200) with rx=150, ry=100
    midpoint_ellipse(325, 200, 150, 100)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"Midpoint Ellipse - OpenGL")
init()
glutDisplayFunc(display)
glutMainLoop()