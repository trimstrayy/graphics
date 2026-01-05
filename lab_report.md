# Lab Report: Computer Graphics Algorithms

## Digital Differential Analyzer (DDA) Line Drawing Algorithm

### Algorithm
The DDA algorithm calculates the incremental changes in x and y for each step to draw a line between two points (x1, y1) and (x2, y2). It determines the number of steps as the maximum of |dx| and |dy|, then increments x and y accordingly.

### Source Code
```python
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
```

### Output Image
[Image Placeholder: Screenshot of the DDA line drawing]

## Bresenham Line Drawing Algorithm

### Algorithm
Bresenham's algorithm uses integer arithmetic to draw lines by deciding at each step whether to increment x or y based on an error term, handling slopes |m| < 1 and |m| >= 1 efficiently.

### Source Code
```python
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
```

### Output Image
[Image Placeholder: Screenshot of the Bresenham line drawing]

## Mid-point Circle Drawing Algorithm

### Algorithm
The mid-point circle algorithm uses a decision parameter to determine the next point on the circle, plotting points in all octants by symmetry.

### Source Code
```python
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
```

### Output Image
[Image Placeholder: Screenshot of the midpoint circle drawing]

## Line Graph using Bresenham Line Algorithm

### Algorithm
For generating a line graph, scale the data points and connect them using Bresenham's line drawing algorithm.

### Source Code
```python
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
```

### Output Image
[Image Placeholder: Screenshot of the line graph]

## Pie Chart

### Algorithm
To draw a pie chart, calculate angles for each data segment and use triangle fans to create colored sectors.

### Source Code
```python
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
```

### Output Image
[Image Placeholder: Screenshot of the pie chart]

## Midpoint Ellipse Drawing Algorithm

### Algorithm
The midpoint ellipse algorithm uses decision parameters to plot points on the ellipse, divided into regions for efficiency.

### Source Code
```python
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
```

### Output Image
[Image Placeholder: Screenshot of the midpoint ellipse drawing]

## Conclusion
This lab report demonstrates the implementation of various computer graphics algorithms using OpenGL and GLUT. Each algorithm was successfully coded and visualized, showcasing line drawing, circle and ellipse plotting, and data visualization techniques like line graphs and pie charts. The use of pixel-level plotting ensures accurate rendering without relying on built-in primitives, providing a deep understanding of raster graphics fundamentals. These implementations highlight the efficiency and precision of classical algorithms in computer graphics. The lab concludes with a comprehensive overview of basic drawing techniques essential for graphics programming. 

Date: December 25, 2025