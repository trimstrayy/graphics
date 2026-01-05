from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_shape(vertices):
    glBegin(GL_POLYGON)
    for v in vertices:
        glVertex2f(v[0], v[1])
    glEnd()

def draw_a(x, y):
    glColor3f(1.0, 0.0, 0.0)
    draw_shape([(x, y), (x + 20, y), (x + 50, y + 100), (x + 30, y + 100)])
    draw_shape([(x + 80, y), (x + 60, y), (x + 30, y + 100), (x + 50, y + 100)])
    draw_shape([(x + 22, y + 35), (x + 58, y + 35), (x + 62, y + 48), (x + 18, y + 48)])

def draw_y(x, y):
    glColor3f(1.0, 0.0, 0.0)
    draw_shape([(x, y + 100), (x + 20, y + 100), (x + 45, y + 50), (x + 30, y + 50)])
    draw_shape([(x + 80, y + 100), (x + 60, y + 100), (x + 35, y + 50), (x + 50, y + 50)])
    draw_shape([(x + 33, y), (x + 47, y), (x + 47, y + 50), (x + 33, y + 50)])

def draw_u(x, y):
    glColor3f(1.0, 0.0, 0.0)
    draw_shape([(x, y + 15), (x + 18, y + 15), (x + 25, y + 100), (x + 7, y + 100)])
    draw_shape([(x + 62, y + 15), (x + 80, y + 15), (x + 73, y + 100), (x + 55, y + 100)])
    draw_shape([(x, y), (x + 80, y), (x + 80, y + 18), (x, y + 18)])

def draw_s(x, y):
    glColor3f(1.0, 0.0, 0.0)
    draw_shape([(x, y + 85), (x + 80, y + 85), (x + 80, y + 100), (x, y + 100)])
    draw_shape([(x, y + 50), (x + 18, y + 50), (x + 18, y + 85), (x, y + 85)])
    draw_shape([(x, y + 35), (x + 80, y + 35), (x + 80, y + 50), (x, y + 50)])
    draw_shape([(x + 62, y + 15), (x + 80, y + 15), (x + 80, y + 35), (x + 62, y + 35)])
    draw_shape([(x, y), (x + 80, y), (x + 80, y + 15), (x, y + 15)])

def draw_h(x, y):
    glColor3f(1.0, 0.0, 0.0)
    draw_shape([(x, y), (x + 18, y), (x + 18, y + 100), (x, y + 100)])
    draw_shape([(x + 62, y), (x + 80, y), (x + 80, y + 100), (x + 62, y + 100)])
    draw_shape([(x + 18, y + 42), (x + 62, y + 42), (x + 62, y + 58), (x + 18, y + 58)])

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    curr_x = 40
    spacing = 100
    y_pos = 150
    
    draw_a(curr_x, y_pos)
    draw_a(curr_x + spacing, y_pos)
    draw_y(curr_x + spacing * 2, y_pos)
    draw_u(curr_x + spacing * 3, y_pos)
    draw_s(curr_x + spacing * 4, y_pos)
    draw_h(curr_x + spacing * 5, y_pos)
    
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 650, 0, 400)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 400)
glutCreateWindow(b"AAYUSH - OpenGL GLPolygons")
init()
glutDisplayFunc(display)
glutMainLoop()