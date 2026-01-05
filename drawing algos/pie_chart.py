from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Implement the Pie chart
def draw_pie_chart(data, colors):
    # data is list of values, colors list of (r,g,b)
    total = sum(data)
    if total == 0:
        return
    start_angle = 0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(325, 200)  # center
    for value, color in zip(data, colors):
        angle = 2 * math.pi * value / total
        end_angle = start_angle + angle
        glColor3f(*color)
        # Draw the sector
        steps = 20
        for i in range(steps + 1):
            a = start_angle + (end_angle - start_angle) * i / steps
            x = 325 + 150 * math.cos(a)
            y = 200 + 150 * math.sin(a)
            glVertex2f(x, y)
        start_angle = end_angle
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Sample data
    data = [10, 20, 30, 40]
    colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0)]
    draw_pie_chart(data, colors)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"Pie Chart - OpenGL")
init()
glutDisplayFunc(display)
glutMainLoop()