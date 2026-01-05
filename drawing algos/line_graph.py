from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Implement the Line Function (DDA/BLA) for generating a line graph of a given set of data
# Using Bresenham Line Algorithm (BLA)
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

def draw_line_graph(data_points):
    # data_points is list of (x, y) tuples
    # Scale to fit in 0-650, 0-400
    if len(data_points) < 2:
        return
    max_y = max(y for x, y in data_points)
    min_y = min(y for x, y in data_points)
    scale_y = 300 / (max_y - min_y) if max_y != min_y else 1
    offset_y = 50
    scale_x = 600 / (len(data_points) - 1) if len(data_points) > 1 else 1
    offset_x = 25
    points = []
    for i, (x, y) in enumerate(data_points):
        px = offset_x + i * scale_x
        py = offset_y + (y - min_y) * scale_y
        points.append((px, py))
    for i in range(len(points) - 1):
        bresenham_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # Sample data
    data = [(0, 1), (1, 3), (2, 2), (3, 5), (4, 4)]
    draw_line_graph(data)
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"Line Graph - OpenGL")
init()
glutDisplayFunc(display)
glutMainLoop()