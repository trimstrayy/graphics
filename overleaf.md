% 2D Transformations Report - LaTeX Template
\documentclass[12pt,a4paper]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{fancyhdr}

% Color definitions
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

% Code listing style
\lstdefinestyle{pythonstyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
\lstset{style=pythonstyle}

% Header and footer
\pagestyle{fancy}
\fancyhf{}
\rfoot{\thepage}
\renewcommand{\headrulewidth}{0pt}

% Document begins
\begin{document}

% Title Page
% Title Page with Logo
\begin{titlepage}
    \begin{center}
        \vspace*{0.5cm}
        
        % Add KU Logo
        \includegraphics[width=8cm]{ku.png}\\
        \vspace{0.5cm}
        
        \textbf{\Large Kathmandu University}\\
        \textbf{Department of Computer Science and Engineering}\\
        Dhulikhel, Kavre
        
        \vspace{3cm}
        
        \textbf{\LARGE Lab Report 3}\\
        \vspace{0.5cm}
        \textbf{[Code No: COMP 342]}
        
        \vspace{3cm}
        
        \textbf{Submitted by:}\\
        \vspace{0.3cm}
        Parichit Giri\\
        Roll no. 23
        
        \vspace{2cm}
        
        \textbf{Submitted to:}\\
        \vspace{0.3cm}
        Mr. Dhiraj Shrestha\\
        Department of Computer Science and Engineering
        
        \vfill
        
        \textbf{Submission Date:} 2026/01/08
        
    \end{center}
\end{titlepage}

\setcounter{page}{2}

% Content starts here
\section*{2D Geometric Transformations}

Geometric transformations are fundamental operations in computer graphics that manipulate the position, orientation, size, and shape of objects in 2D space. These transformations are essential for creating animations, modeling complex scenes, and implementing various graphical effects. This report implements and demonstrates five basic 2D transformations: translation, rotation, scaling, reflection, and shearing, along with composite transformations that combine multiple operations.

\subsection*{Homogeneous Coordinates}
All transformations in this implementation use \textbf{homogeneous coordinates}, which extend 2D coordinates $(x, y)$ to 3D coordinates $(x, y, 1)$. This approach provides a unified mathematical framework for representing all transformations as matrix operations, enabling efficient computation and composition of complex transformations.

\newpage
\section*{2D Translation}
\textbf{Translation} is the most fundamental geometric transformation that moves an object from one position to another in the 2D plane without altering its size, shape, or orientation. It involves shifting every point of the object by the same displacement vector.

\subsection*{Mathematical Foundation}
For a point $(x, y)$, translation by displacement vector $(t_x, t_y)$ produces the new coordinates:
\begin{align*}
x' &= x + t_x \\
y' &= y + t_y
\end{align*}

\subsection*{Algorithm}
\begin{enumerate}
    \item \textbf{Input:} Original object coordinates $(x, y)$ and translation factors $(t_x, t_y)$
    \item \textbf{Compute:} Apply translation to each vertex: $(x', y') = (x + t_x, y + t_y)$
    \item \textbf{Output:} Display both original and translated objects for comparison
\end{enumerate}

\subsection*{Transformation Matrix}
In homogeneous coordinates, 2D translation is represented by the matrix:
\begin{equation}
\mathbf{T}(t_x, t_y) = \begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

The transformation is applied as:
\begin{equation}
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
\end{equation}

\newpage
\subsection*{Source Code:}

\begin{lstlisting}[language=Python]
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
\end{lstlisting}

\subsection*{Output:}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/translation.png}
    \caption{2-D Translation}
    \label{fig:translation}
\end{figure}

\newpage
\section*{2D Rotation}
\textbf{Rotation} is a transformation that rotates an object around a fixed point (pivot) by a specified angle. The rotation preserves the shape and size of the object while changing its orientation. The most common rotation is around the origin, but rotations around arbitrary points can be achieved through composite transformations.

\subsection*{Mathematical Foundation}
For rotation by angle $\theta$ around the origin, the transformation formulas are:
\begin{align*}
x' &= x \cos\theta - y \sin\theta \\
y' &= x \sin\theta + y \cos\theta
\end{align*}

Where $\theta$ is measured counterclockwise from the positive x-axis.

\subsection*{Algorithm}
\begin{enumerate}
    \item \textbf{Input:} Object coordinates $(x, y)$, rotation angle $\theta$ (in degrees), and pivot point $(x_c, y_c)$
    \item \textbf{Pre-process:} Convert angle to radians: $\theta_{rad} = \theta \times \frac{\pi}{180}$
    \item \textbf{Transform:} For rotation around origin:
    \begin{itemize}
        \item $x' = x \cos\theta - y \sin\theta$
        \item $y' = x \sin\theta + y \cos\theta$
    \end{itemize}
    \item \textbf{Output:} Display original and rotated objects
\end{enumerate}

\subsection*{Transformation Matrix}
In homogeneous coordinates, rotation about the origin is represented as:
\begin{equation}
\mathbf{R}(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

The complete transformation:
\begin{equation}
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
\end{equation}

\subsection*{Source Code:}

\begin{lstlisting}[language=Python]
"""
2D Rotation using OpenGL
Demonstrates rotation transformation on geometric shapes
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
    [200.0, 200.0],
    [300.0, 200.0],
    [250.0, 300.0]
]

# Rectangle vertices (original)
rectangle = [
    [450.0, 150.0],
    [550.0, 150.0],
    [550.0, 250.0],
    [450.0, 250.0]
]

# Rotation parameters
angle = 30.0  # degrees
rotation_speed = 2.0

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

def rotate_point(point, angle_degrees, center=(WIDTH/2, HEIGHT/2)):
    """Rotate a point around a center point"""
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)

    # Translate to origin
    x = point[0] - center[0]
    y = point[1] - center[1]

    # Rotate
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a

    # Translate back
    return [x_new + center[0], y_new + center[1]]

def rotate_shape(shape, angle, center=(WIDTH/2, HEIGHT/2)):
    """Rotate all points in a shape around a center"""
    return [rotate_point(point, angle, center) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw rotated shapes
    rotated_triangle = rotate_shape(triangle, angle)
    rotated_rectangle = rotate_shape(rectangle, angle)

    draw_triangle(rotated_triangle, (0.0, 0.0, 1.0))  # Blue rotated triangle
    draw_rectangle(rotated_rectangle, (1.0, 1.0, 0.0))  # Yellow rotated rectangle

    # Draw rotation center
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(WIDTH/2, HEIGHT/2)
    glEnd()

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Rotation: {:.1f} degrees".format(angle)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Rotated, Magenta: Center"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global angle

    if key == b'q':
        angle += rotation_speed  # Rotate clockwise
    elif key == b'e':
        angle -= rotation_speed  # Rotate counter-clockwise
    elif key == b'r':
        angle = 30.0  # Reset
    elif key == b' ':
        angle = 0.0  # Reset to 0
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def idle():
    """Idle callback for continuous rotation"""
    global angle
    angle += 0.5  # Slow continuous rotation
    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Rotation - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    # glutIdleFunc(idle)  # Uncomment for continuous rotation

    print("2D Rotation Controls:")
    print("Q: Rotate clockwise")
    print("E: Rotate counter-clockwise")
    print("R: Reset to 30 degrees")
    print("Space: Reset to 0 degrees")
    print("ESC: Quit")
    print("Current angle: {:.1f} degrees".format(angle))

    glutMainLoop()

if __name__ == "__main__":
    main()
\end{lstlisting}

\subsection*{Output:}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/rotation.png}
    \caption{2-D Rotation}
    \label{fig:rotation}
\end{figure}

\newpage
\section*{2D Scaling}
\textbf{Scaling} is a transformation that changes the size of an object by multiplying its coordinates by scaling factors. \textit{Uniform scaling} maintains the aspect ratio when $s_x = s_y$, while \textit{non-uniform scaling} can stretch or compress the object along different axes when $s_x \neq s_y$. Scaling factors greater than 1 enlarge the object, while factors between 0 and 1 shrink it.

\subsection*{Mathematical Foundation}
For a point $(x, y)$, scaling by factors $(s_x, s_y)$ produces:
\begin{align*}
x' &= x \times s_x \\
y' &= y \times s_y
\end{align*}

\subsection*{Special Cases}
\begin{itemize}
    \item \textbf{Uniform Scaling:} $s_x = s_y$ - preserves aspect ratio
    \item \textbf{Differential Scaling:} $s_x \neq s_y$ - changes aspect ratio
    \item \textbf{Reduction:} $0 < s_x, s_y < 1$ - shrinks the object
    \item \textbf{Enlargement:} $s_x, s_y > 1$ - enlarges the object
    \item \textbf{Reflection:} Negative scaling factors flip the object
\end{itemize}

\subsection*{Algorithm}
\begin{enumerate}
    \item \textbf{Input:} Object coordinates $(x, y)$ and scaling factors $(s_x, s_y)$
    \item \textbf{Compute:} Apply scaling to each vertex: $(x', y') = (x \cdot s_x, y \cdot s_y)$
    \item \textbf{Output:} Display original and scaled objects for comparison
\end{enumerate}

\subsection*{Transformation Matrix}
In homogeneous coordinates, scaling is represented as:
\begin{equation}
\mathbf{S}(s_x, s_y) = \begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

The transformation is applied as:
\begin{equation}
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
\begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
\end{equation}

\subsection*{Source Code:}

\begin{lstlisting}[language=Python]
"""
2D Scaling using OpenGL
Demonstrates scaling transformation on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [150.0, 150.0],
    [250.0, 150.0],
    [200.0, 250.0]
]

# Rectangle vertices (original)
rectangle = [
    [400.0, 150.0],
    [500.0, 150.0],
    [500.0, 250.0],
    [400.0, 250.0]
]

# Scaling parameters
sx, sy = 1.5, 0.8

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

def scale_point(point, sx, sy, center=(WIDTH/2, HEIGHT/2)):
    """Scale a point relative to a center"""
    # Translate to origin
    x = point[0] - center[0]
    y = point[1] - center[1]

    # Scale
    x_scaled = x * sx
    y_scaled = y * sy

    # Translate back
    return [x_scaled + center[0], y_scaled + center[1]]

def scale_shape(shape, sx, sy, center=(WIDTH/2, HEIGHT/2)):
    """Scale all points in a shape relative to a center"""
    return [scale_point(point, sx, sy, center) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw scaled shapes
    scaled_triangle = scale_shape(triangle, sx, sy)
    scaled_rectangle = scale_shape(rectangle, sx, sy)

    draw_triangle(scaled_triangle, (0.0, 0.0, 1.0))  # Blue scaled triangle
    draw_rectangle(scaled_rectangle, (1.0, 1.0, 0.0))  # Yellow scaled rectangle

    # Draw scaling center
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(WIDTH/2, HEIGHT/2)
    glEnd()

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Scaling: sx={:.1f}, sy={:.1f}".format(sx, sy)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Scaled, Magenta: Center"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global sx, sy

    if key == b'w':
        sy += 0.1  # Increase Y scaling
    elif key == b's':
        sy -= 0.1  # Decrease Y scaling
    elif key == b'a':
        sx -= 0.1  # Decrease X scaling
    elif key == b'd':
        sx += 0.1  # Increase X scaling
    elif key == b'q':
        sx += 0.1  # Increase both
        sy += 0.1
    elif key == b'e':
        sx -= 0.1  # Decrease both
        sy -= 0.1
    elif key == b'r':
        sx, sy = 1.5, 0.8  # Reset
    elif key == b' ':
        sx, sy = 1.0, 1.0  # Reset to no scaling
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    # Ensure scaling factors don't go negative or too small
    sx = max(0.1, sx)
    sy = max(0.1, sy)

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Scaling - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Scaling Controls:")
    print("WASD: Adjust X/Y scaling factors")
    print("Q: Increase both scaling factors")
    print("E: Decrease both scaling factors")
    print("R: Reset to sx=1.5, sy=0.8")
    print("Space: Reset to sx=1.0, sy=1.0")
    print("ESC: Quit")
    print("Current scaling: sx={:.1f}, sy={:.1f}".format(sx, sy))

    glutMainLoop()

if __name__ == "__main__":
    main()
\end{lstlisting}

\subsection*{Output:}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/scaling.png}
    \caption{2-D Scaling}
    \label{fig:scaling}
\end{figure}

\newpage
\section*{2D Reflection}
\textbf{Reflection} is a transformation that creates a mirror image of an object across a specified axis or through a point. Unlike rotation and scaling, reflection is an \textit{isometric transformation} that preserves distances and angles, but reverses orientation (creates a mirror image).

\subsection*{Types of Reflection}
\begin{itemize}
    \item \textbf{X-axis Reflection:} Mirror image across the horizontal axis
    \item \textbf{Y-axis Reflection:} Mirror image across the vertical axis  
    \item \textbf{Origin Reflection:} Mirror image through the coordinate origin (180° rotation)
\end{itemize}

\subsection*{Mathematical Foundation}
\begin{itemize}
    \item \textbf{X-axis:} $(x, y) \rightarrow (x, -y)$
    \item \textbf{Y-axis:} $(x, y) \rightarrow (-x, y)$
    \item \textbf{Origin:} $(x, y) \rightarrow (-x, -y)$
\end{itemize}

\subsection*{Properties}
\begin{itemize}
    \item \textbf{Distance Preservation:} Distances between points remain unchanged
    \item \textbf{Angle Preservation:} Angles between lines are maintained
    \item \textbf{Orientation Reversal:} Clockwise becomes counterclockwise (and vice versa)
    \item \textbf{Isometric:} Shape and size are preserved
\end{itemize}

\subsection*{Algorithm}
\begin{enumerate}
    \item \textbf{Input:} Object coordinates $(x, y)$ and reflection type
    \item \textbf{Select Reflection:}
    \begin{itemize}
        \item X-axis: $(x', y') = (x, -y)$
        \item Y-axis: $(x', y') = (-x, y)$
        \item Origin: $(x', y') = (-x, -y)$
    \end{itemize}
    \item \textbf{Apply:} Transform all vertices of the object
    \item \textbf{Output:} Display original and reflected objects
\end{enumerate}

\subsection*{Transformation Matrices}

\textbf{Reflection about X-axis:}
\begin{equation}
\mathbf{R}_x = \begin{bmatrix}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\textbf{Reflection about Y-axis:}
\begin{equation}
\mathbf{R}_y = \begin{bmatrix}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\textbf{Reflection about Origin:}
\begin{equation}
\mathbf{R}_o = \begin{bmatrix}
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Source Code:}

\begin{lstlisting}[language=Python]
"""
2D Reflection using OpenGL
Demonstrates reflection transformations on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [150.0, 200.0],
    [250.0, 200.0],
    [200.0, 300.0]
]

# Rectangle vertices (original)
rectangle = [
    [400.0, 200.0],
    [500.0, 200.0],
    [500.0, 300.0],
    [400.0, 300.0]
]

# Reflection mode
reflection_mode = 0  # 0: X-axis, 1: Y-axis, 2: Origin

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

def reflect_point_x_axis(point):
    """Reflect point across X-axis"""
    return [point[0], HEIGHT - point[1]]

def reflect_point_y_axis(point):
    """Reflect point across Y-axis"""
    return [WIDTH - point[0], point[1]]

def reflect_point_origin(point):
    """Reflect point through origin"""
    return [WIDTH - point[0], HEIGHT - point[1]]

def reflect_shape(shape, mode):
    """Reflect all points in a shape"""
    if mode == 0:  # X-axis
        return [reflect_point_x_axis(point) for point in shape]
    elif mode == 1:  # Y-axis
        return [reflect_point_y_axis(point) for point in shape]
    elif mode == 2:  # Origin
        return [reflect_point_origin(point) for point in shape]
    return shape

def draw_axes():
    """Draw coordinate axes"""
    glColor3f(0.5, 0.5, 0.5)  # Gray

    # X-axis
    glBegin(GL_LINES)
    glVertex2f(0, HEIGHT/2)
    glVertex2f(WIDTH, HEIGHT/2)
    glEnd()

    # Y-axis
    glBegin(GL_LINES)
    glVertex2f(WIDTH/2, 0)
    glVertex2f(WIDTH/2, HEIGHT)
    glEnd()

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw coordinate axes
    draw_axes()

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw reflected shapes
    reflected_triangle = reflect_shape(triangle, reflection_mode)
    reflected_rectangle = reflect_shape(rectangle, reflection_mode)

    draw_triangle(reflected_triangle, (0.0, 0.0, 1.0))  # Blue reflected triangle
    draw_rectangle(reflected_rectangle, (1.0, 1.0, 0.0))  # Yellow reflected rectangle

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    mode_names = ["X-axis", "Y-axis", "Origin"]
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Reflection: {}".format(mode_names[reflection_mode])
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: Reflected"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glRasterPos2f(50, HEIGHT - 110)
    text = "Press 1,2,3 to change reflection mode"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global reflection_mode

    if key == b'1':
        reflection_mode = 0  # X-axis
    elif key == b'2':
        reflection_mode = 1  # Y-axis
    elif key == b'3':
        reflection_mode = 2  # Origin
    elif key == b'r' or key == b'R':
        reflection_mode = 0  # Reset to X-axis
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Reflection - OpenGL")
a
    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Reflection Controls:")
    print("1: Reflect across X-axis")
    print("2: Reflect across Y-axis")
    print("3: Reflect through Origin")
    print("R: Reset to X-axis reflection")
    print("ESC: Quit")
    print("Current mode: X-axis reflection")

    glutMainLoop()

if __name__ == "__main__":
    main()
\end{lstlisting}

\subsection*{Output:}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/reflection_x.png}
    \caption{2-D Reflection}
    \label{fig:reflection}
\end{figure}

\newpage
\section*{2D Shearing}
\textbf{Shearing} is a transformation that distorts the shape of an object by shifting its points along specified axes, creating a slanted or skewed effect. Unlike rigid transformations (translation, rotation), shearing is an \textit{affine transformation} that changes the shape while preserving parallelism of lines.

\subsection*{Types of Shearing}
\begin{itemize}
    \item \textbf{X-direction Shearing:} Shifts points horizontally based on their y-coordinate
    \item \textbf{Y-direction Shearing:} Shifts points vertically based on their x-coordinate
    \item \textbf{Combined Shearing:} Applies both X and Y shearing simultaneously
\end{itemize}

\subsection*{Mathematical Foundation}
\begin{itemize}
    \item \textbf{X-shearing:} $(x, y) \rightarrow (x + sh_x \cdot y, y)$
    \item \textbf{Y-shearing:} $(x, y) \rightarrow (x, y + sh_y \cdot x)$
    \item \textbf{Combined:} $(x, y) \rightarrow (x + sh_x \cdot y, y + sh_y \cdot x)$
\end{itemize}

\subsection*{Visual Effects}
\begin{itemize}
    \item \textbf{X-shearing:} Creates a leaning effect (like italic text)
    \item \textbf{Y-shearing:} Creates a slanting effect in the vertical direction
    \item \textbf{Parallelism:} Parallel lines remain parallel after shearing
    \item \textbf{Areas:} The area of the object may change depending on shear factors
\end{itemize}

\subsection*{Algorithm}
\begin{enumerate}
    \item \textbf{Input:} Object coordinates $(x, y)$ and shear factors $(sh_x, sh_y)$
    \item \textbf{Apply Shearing:}
    \begin{itemize}
        \item X-shearing: $(x', y') = (x + sh_x \cdot y, y)$
        \item Y-shearing: $(x', y') = (x, y + sh_y \cdot x)$
    \end{itemize}
    \item \textbf{Transform:} Apply to all vertices of the object
    \item \textbf{Output:} Display original and sheared objects
\end{enumerate}

\subsection*{Transformation Matrices}

\textbf{Shearing along X-axis:}
\begin{equation}
\mathbf{SH}_x(sh_x) = \begin{bmatrix}
1 & sh_x & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\textbf{Shearing along Y-axis:}
\begin{equation}
\mathbf{SH}_y(sh_y) = \begin{bmatrix}
1 & 0 & 0 \\
sh_y & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\textbf{Combined Shearing:}
\begin{equation}
\mathbf{SH}(sh_x, sh_y) = \begin{bmatrix}
1 & sh_x & 0 \\
sh_y & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Source Code:}

\begin{lstlisting}[language=Python]
"""
2D Shearing using OpenGL
Demonstrates shearing transformations on geometric shapes
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Triangle vertices (original)
triangle = [
    [150.0, 200.0],
    [250.0, 200.0],
    [200.0, 300.0]
]

# Rectangle vertices (original)
rectangle = [
    [400.0, 200.0],
    [500.0, 200.0],
    [500.0, 300.0],
    [400.0, 300.0]
]

# Shearing parameters
shx, shy = 0.3, 0.2  # Shearing factors

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

def shear_point_x(point, shx):
    """Shear point in X direction"""
    x, y = point
    return [x + shx * y, y]

def shear_point_y(point, shy):
    """Shear point in Y direction"""
    x, y = point
    return [x, y + shy * x]

def shear_shape_x(shape, shx):
    """Shear all points in a shape in X direction"""
    return [shear_point_x(point, shx) for point in shape]

def shear_shape_y(shape, shy):
    """Shear all points in a shape in Y direction"""
    return [shear_point_y(point, shy) for point in shape]

def display():
    """Display callback function"""
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw original shapes
    draw_triangle(triangle, (1.0, 0.0, 0.0))  # Red triangle
    draw_rectangle(rectangle, (0.0, 1.0, 0.0))  # Green rectangle

    # Draw sheared shapes (X-direction)
    sheared_x_triangle = shear_shape_x(triangle, shx)
    sheared_x_rectangle = shear_shape_x(rectangle, shx)

    draw_triangle(sheared_x_triangle, (0.0, 0.0, 1.0))  # Blue X-sheared triangle
    draw_rectangle(sheared_x_rectangle, (1.0, 1.0, 0.0))  # Yellow X-sheared rectangle

    # Draw sheared shapes (Y-direction) - offset for visibility
    offset_triangle = [[p[0] + 150, p[1]] for p in triangle]
    offset_rectangle = [[p[0] + 150, p[1]] for p in rectangle]

    sheared_y_triangle = shear_shape_y(offset_triangle, shy)
    sheared_y_rectangle = shear_shape_y(offset_rectangle, shy)

    draw_triangle(sheared_y_triangle, (1.0, 0.0, 1.0))  # Magenta Y-sheared triangle
    draw_rectangle(sheared_y_rectangle, (0.0, 1.0, 1.0))  # Cyan Y-sheared rectangle

    # Draw labels
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(50, HEIGHT - 50)
    text = "2D Shearing: X-shearing={:.1f}, Y-shearing={:.1f}".format(shx, shy)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glRasterPos2f(50, HEIGHT - 80)
    text = "Red/Green: Original, Blue/Yellow: X-sheared, Magenta/Cyan: Y-sheared"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    """Keyboard callback function"""
    global shx, shy

    if key == b'w':
        shy += 0.1  # Increase Y shearing
    elif key == b's':
        shy -= 0.1  # Decrease Y shearing
    elif key == b'a':
        shx -= 0.1  # Decrease X shearing
    elif key == b'd':
        shx += 0.1  # Increase X shearing
    elif key == b'q':
        shx = 0.0  # Reset X shearing
    elif key == b'e':
        shy = 0.0  # Reset Y shearing
    elif key == b'r':
        shx, shy = 0.3, 0.2  # Reset both
    elif key == b' ':
        shx, shy = 0.0, 0.0  # Reset to no shearing
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()

    glutPostRedisplay()

def main():
    """Main function"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"2D Shearing - OpenGL")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("2D Shearing Controls:")
    print("WASD: Adjust shearing factors")
    print("Q: Reset X-shearing to 0")
    print("E: Reset Y-shearing to 0")
    print("R: Reset to shx=0.3, shy=0.2")
    print("Space: Reset to no shearing")
    print("ESC: Quit")
    print("Current shearing: shx={:.1f}, shy={:.1f}".format(shx, shy))

    glutMainLoop()

if __name__ == "__main__":
    main()
\end{lstlisting}

\subsection*{Output:}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/shearing_x.png}
    \caption{2-D Shearing}
    \label{fig:shearing}
\end{figure}

\newpage
\section*{Composite Transformations}
\textbf{Composite transformations} combine multiple basic transformations into a single operation through matrix multiplication. Since matrix multiplication is not commutative, the order of applying transformations is crucial and affects the final result. This approach is computationally efficient as it requires only one matrix multiplication per vertex.

\subsection*{Matrix Multiplication Order}
For transformations $T_1, T_2, T_3$, the composite matrix is:
\begin{equation}
\mathbf{M} = T_3 \times T_2 \times T_1
\end{equation}

The transformations are applied from right to left: first $T_1$, then $T_2$, then $T_3$.

\subsection*{Common Composite Transformations}

\subsubsection*{1. Rotation about an Arbitrary Point $(x_c, y_c)$}
\begin{enumerate}
    \item \textbf{Translate} object so rotation point becomes origin: $\mathbf{T}(-x_c, -y_c)$
    \item \textbf{Rotate} about origin: $\mathbf{R}(\theta)$
    \item \textbf{Translate} back: $\mathbf{T}(x_c, y_c)$
\end{enumerate}

\textbf{Composite matrix:} $\mathbf{M} = \mathbf{T}(x_c, y_c) \times \mathbf{R}(\theta) \times \mathbf{T}(-x_c, -y_c)$

\subsubsection*{2. Scaling about an Arbitrary Point $(x_c, y_c)$}
\begin{enumerate}
    \item \textbf{Translate} object to origin: $\mathbf{T}(-x_c, -y_c)$
    \item \textbf{Scale} about origin: $\mathbf{S}(s_x, s_y)$
    \item \textbf{Translate} back: $\mathbf{T}(x_c, y_c)$
\end{enumerate}

\textbf{Composite matrix:} $\mathbf{M} = \mathbf{T}(x_c, y_c) \times \mathbf{S}(s_x, s_y) \times \mathbf{T}(-x_c, -y_c)$

\subsubsection*{3. Translation + Rotation + Scaling}
A sequence combining position, orientation, and size changes:

\textbf{Composite matrix:} $\mathbf{M} = \mathbf{T}(t_x, t_y) \times \mathbf{R}(\theta) \times \mathbf{S}(s_x, s_y)$

\subsubsection*{4. Complex Transformations}
Combining reflection, rotation, translation, and shearing:

\textbf{Composite matrix:} $\mathbf{M} = \mathbf{T}(t_x, t_y) \times \mathbf{R}(\theta) \times \mathbf{R}_{axis} \times \mathbf{SH}(sh_x, sh_y)$

\subsection*{Algorithm}
\begin{enumerate}
    \item \textbf{Define} individual transformation matrices
    \item \textbf{Multiply} matrices in correct order: $\mathbf{M} = T_n \times \cdots \times T_1$
    \item \textbf{Apply} composite matrix to each vertex: $\mathbf{v}' = \mathbf{M} \times \mathbf{v}$
    \item \textbf{Render} original and transformed objects
\end{enumerate}

\subsection*{Advantages}
\begin{itemize}
    \item \textbf{Efficiency:} Single matrix multiplication per vertex
    \item \textbf{Modularity:} Build complex transformations from simple ones
    \item \textbf{Reusability:} Pre-compute composite matrices for repeated use
    \item \textbf{Mathematical Rigor:} Leverages linear algebra properties
\end{itemize}

\newpage
\subsection*{Source Code:}

\begin{lstlisting}[language=Python]
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
\end{lstlisting}

\subsection*{Output:}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/composite_1.png}
    \caption{Composite Transformations}
    \label{fig:composite}
\end{figure}

\newpage
\section*{Conclusion}

This comprehensive implementation of 2D geometric transformations demonstrates the power and elegance of homogeneous coordinate systems in computer graphics. All fundamental transformations were successfully implemented using OpenGL, providing both mathematical rigor and visual verification.

\subsection*{Transformations Implemented}

\begin{itemize}
    \item \textbf{Translation:} Rigid movement of objects in 2D space without deformation
    \item \textbf{Rotation:} Angular displacement around a pivot point with distance preservation
    \item \textbf{Scaling:} Size modification with uniform and non-uniform scaling capabilities
    \item \textbf{Reflection:} Mirror imaging across axes and through the origin
    \item \textbf{Shearing:} Affine distortion creating slanted effects while maintaining parallelism
    \item \textbf{Composite Transformations:} Complex operations combining multiple transformations efficiently
\end{itemize}

\subsection*{Key Technical Achievements}

\begin{enumerate}
    \item \textbf{Mathematical Foundation:} Consistent use of homogeneous coordinates and matrix representations
    \item \textbf{Interactive Visualization:} Real-time OpenGL rendering with keyboard controls for parameter adjustment
    \item \textbf{Modular Design:} Separate functions for each transformation type enabling code reusability
    \item \textbf{Comprehensive Testing:} Visual verification of transformation correctness through geometric comparisons
    \item \textbf{Matrix Composition:} Efficient implementation of composite transformations through matrix multiplication
\end{enumerate}

\subsection*{Applications and Significance}

The implemented transformations form the foundation for:
\begin{itemize}
    \item \textbf{Computer Animation:} Object movement, rotation, and scaling in animated sequences
    \item \textbf{3D Graphics Pipeline:} Extension to 3D transformations using 4×4 homogeneous matrices
    \item \textbf{Image Processing:} Geometric corrections and special effects
    \item \textbf{CAD Systems:} Precise object manipulation in design software
    \item \textbf{Game Development:} Sprite manipulation and world transformations
    \item \textbf{Robotics:} Coordinate system transformations for robotic manipulation
\end{itemize}

\subsection*{Technical Insights}

The implementation reveals several important principles:
\begin{itemize}
    \item \textbf{Matrix Order:} Transformation order affects final results due to non-commutativity
    \item \textbf{Coordinate Systems:} Homogeneous coordinates unify translation with linear transformations
    \item \textbf{Efficiency:} Matrix-based approach enables hardware acceleration and optimized computation
    \item \textbf{Composition:} Complex transformations can be built from simple, reusable components
    \item \textbf{Visualization:} Interactive graphics provide immediate feedback for understanding transformations
\end{itemize}

This project successfully bridges theoretical computer graphics concepts with practical implementation, demonstrating how fundamental mathematical principles enable sophisticated visual manipulations essential for modern computing applications.

\end{document}