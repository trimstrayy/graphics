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

Geometric transformations are fundamental operations in computer graphics that manipulate the position, orientation, size, and shape of objects in 2D space. This report implements and demonstrates five basic 2D transformations: translation, rotation, scaling, reflection, and shearing, using homogeneous coordinate systems.

\subsection*{Homogeneous Coordinates}
All transformations use homogeneous coordinates, extending 2D coordinates $(x, y)$ to 3D coordinates $(x, y, 1)$, providing a unified mathematical framework for all transformations as matrix operations.

\newpage
\section*{2D Translation}
\textbf{Translation} moves an object from one position to another without changing its size, shape, or orientation.

\subsection*{Algorithm}
\begin{enumerate}
    \item Input object coordinates $(x, y)$ and translation factors $(t_x, t_y)$
    \item Apply: $x' = x + t_x$, $y' = y + t_y$
    \item Display original and translated objects
\end{enumerate}

\subsection*{Transformation Matrix}
\begin{equation}
\mathbf{T}(t_x, t_y) = \begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Implementation}
\begin{lstlisting}[language=Python]
import numpy as np

def translate_point(point, tx, ty):
    """Translate a point by tx, ty"""
    x, y = point
    return [x + tx, y + ty]

def translate_shape(shape, tx, ty):
    """Translate all points in shape"""
    return [translate_point(p, tx, ty) for p in shape]

# Example usage
triangle = [[2, 2], [6, 2], [4, 6]]
translated = translate_shape(triangle, 3, 4)
\end{lstlisting}

\subsection*{Output}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/translation.png}
    \caption{2D Translation (tx=50, ty=30)}
    \label{fig:translation}
\end{figure}

\newpage
\section*{2D Rotation}
\textbf{Rotation} rotates an object around a fixed point by a specified angle, preserving shape and size.

\subsection*{Algorithm}
\begin{enumerate}
    \item Input coordinates $(x, y)$, angle $\theta$, and center $(x_c, y_c)$
    \item Convert angle to radians: $\theta_{rad} = \theta \times \pi/180$
    \item Apply: $x' = (x - x_c)\cos\theta - (y - y_c)\sin\theta + x_c$
    \item Apply: $y' = (x - x_c)\sin\theta + (y - y_c)\cos\theta + y_c$
\end{enumerate}

\subsection*{Transformation Matrix}
\begin{equation}
\mathbf{R}(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Implementation}
\begin{lstlisting}[language=Python]
import math

def rotate_point(point, angle_deg, center=(0, 0)):
    """Rotate point around center"""
    x, y = point
    cx, cy = center
    angle_rad = math.radians(angle_deg)

    # Translate to origin
    x -= cx
    y -= cy

    # Rotate
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)

    # Translate back
    return [x_new + cx, y_new + cy]

def rotate_shape(shape, angle, center=(400, 300)):
    """Rotate all points in shape"""
    return [rotate_point(p, angle, center) for p in shape]

# Example usage
rectangle = [[350, 250], [450, 250], [450, 350], [350, 350]]
rotated = rotate_shape(rectangle, 30)
\end{lstlisting}

\subsection*{Output}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/rotation.png}
    \caption{2D Rotation (30 degrees around center)}
    \label{fig:rotation}
\end{figure}

\newpage
\section*{2D Scaling}
\textbf{Scaling} changes object size by multiplying coordinates by scaling factors.

\subsection*{Algorithm}
\begin{enumerate}
    \item Input coordinates $(x, y)$ and scaling factors $(s_x, s_y)$
    \item Apply: $x' = x \times s_x$, $y' = y \times s_y$
    \item Display original and scaled objects
\end{enumerate}

\subsection*{Transformation Matrix}
\begin{equation}
\mathbf{S}(s_x, s_y) = \begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Implementation}
\begin{lstlisting}[language=Python]
def scale_point(point, sx, sy, center=(400, 300)):
    """Scale point relative to center"""
    x, y = point
    cx, cy = center

    # Translate to origin
    x -= cx
    y -= cy

    # Scale
    x_scaled = x * sx
    y_scaled = y * sy

    # Translate back
    return [x_scaled + cx, y_scaled + cy]

def scale_shape(shape, sx, sy, center=(400, 300)):
    """Scale all points in shape"""
    return [scale_point(p, sx, sy, center) for p in shape]

# Example usage
triangle = [[350, 250], [450, 250], [400, 350]]
scaled = scale_shape(triangle, 1.5, 0.8)
\end{lstlisting}

\subsection*{Output}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/scaling.png}
    \caption{2D Scaling (sx=1.5, sy=0.8)}
    \label{fig:scaling}
\end{figure}

\newpage
\section*{2D Reflection}
\textbf{Reflection} creates mirror images across specified axes or through points.

\subsection*{Algorithm}
\begin{enumerate}
    \item Select reflection type (X-axis, Y-axis, or origin)
    \item Apply appropriate formula:
    \begin{itemize}
        \item X-axis: $(x, y) \rightarrow (x, -y)$
        \item Y-axis: $(x, y) \rightarrow (-x, y)$
        \item Origin: $(x, y) \rightarrow (-x, -y)$
    \end{itemize}
\end{enumerate}

\subsection*{Transformation Matrices}
\begin{equation}
\mathbf{R}_x = \begin{bmatrix}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{bmatrix}, \quad
\mathbf{R}_y = \begin{bmatrix}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}, \quad
\mathbf{R}_o = \begin{bmatrix}
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Implementation}
\begin{lstlisting}[language=Python]
def reflect_x_axis(point):
    """Reflect across X-axis"""
    x, y = point
    return [x, -y]

def reflect_y_axis(point):
    """Reflect across Y-axis"""
    x, y = point
    return [-x, y]

def reflect_origin(point):
    """Reflect through origin"""
    x, y = point
    return [-x, -y]

def reflect_shape(shape, mode):
    """Reflect shape based on mode"""
    if mode == 'x':
        return [reflect_x_axis(p) for p in shape]
    elif mode == 'y':
        return [reflect_y_axis(p) for p in shape]
    elif mode == 'origin':
        return [reflect_origin(p) for p in shape]

# Example usage
triangle = [[350, 250], [450, 250], [400, 350]]
reflected = reflect_shape(triangle, 'x')
\end{lstlisting}

\subsection*{Output}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/reflection_x.png}
    \caption{2D Reflection across X-axis}
    \label{fig:reflection}
\end{figure}

\newpage
\section*{2D Shearing}
\textbf{Shearing} distorts objects by shifting points along specified axes.

\subsection*{Algorithm}
\begin{enumerate}
    \item Input coordinates $(x, y)$ and shear factors $(sh_x, sh_y)$
    \item Apply shearing formulas:
    \begin{itemize}
        \item X-shear: $(x, y) \rightarrow (x + sh_x \cdot y, y)$
        \item Y-shear: $(x, y) \rightarrow (x, y + sh_y \cdot x)$
    \end{itemize}
\end{enumerate}

\subsection*{Transformation Matrices}
\begin{equation}
\mathbf{SH}_x(sh_x) = \begin{bmatrix}
1 & sh_x & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}, \quad
\mathbf{SH}_y(sh_y) = \begin{bmatrix}
1 & 0 & 0 \\
sh_y & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\end{equation}

\subsection*{Implementation}
\begin{lstlisting}[language=Python]
def shear_x(point, shx):
    """Shear in X direction"""
    x, y = point
    return [x + shx * y, y]

def shear_y(point, shy):
    """Shear in Y direction"""
    x, y = point
    return [x, y + shy * x]

def shear_shape_x(shape, shx):
    """Apply X-shearing to shape"""
    return [shear_x(p, shx) for p in shape]

def shear_shape_y(shape, shy):
    """Apply Y-shearing to shape"""
    return [shear_y(p, shy) for p in shape]

# Example usage
rectangle = [[350, 250], [450, 250], [450, 350], [350, 350]]
sheared = shear_shape_x(rectangle, 0.3)
\end{lstlisting}

\subsection*{Output}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/shearing_x.png}
    \caption{2D X-Shearing (shx=0.3)}
    \label{fig:shearing}
\end{figure}

\newpage
\section*{Composite Transformations}
\textbf{Composite transformations} combine multiple transformations through matrix multiplication.

\subsection*{Algorithm}
\begin{enumerate}
    \item Define transformation matrices $(T_1, T_2, \ldots, T_n)$
    \item Compute composite matrix: $M = T_n \times \cdots \times T_1$
    \item Apply to each vertex: $v' = M \times v$
\end{enumerate}

\subsection*{Examples}
\begin{itemize}
    \item Rotation about arbitrary point: $M = T(x_c, y_c) \times R(\theta) \times T(-x_c, -y_c)$
    \item Scaling about arbitrary point: $M = T(x_c, y_c) \times S(s_x, s_y) \times T(-x_c, -y_c)$
\end{itemize}

\subsection*{Implementation}
\begin{lstlisting}[language=Python]
import numpy as np

def translation_matrix(tx, ty):
    return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

def rotation_matrix(angle_deg):
    theta = np.radians(angle_deg)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def scale_matrix(sx, sy):
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

def apply_transformation(points, matrix):
    """Apply transformation matrix to points"""
    homogeneous = np.column_stack([points, np.ones(len(points))])
    transformed = (matrix @ homogeneous.T).T
    return transformed[:, :2]

# Example: Rotation about point (4, 3)
triangle = np.array([[2, 2], [6, 2], [4, 6]])
center = np.array([4, 3])

# Composite: Translate to origin, rotate, translate back
M = (translation_matrix(center[0], center[1]) @
     rotation_matrix(45) @
     translation_matrix(-center[0], -center[1]))

transformed = apply_transformation(triangle, M)
\end{lstlisting}

\subsection*{Output}
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\linewidth]{plots/composite_1.png}
    \caption{Composite Transformation: Rotation about arbitrary point}
    \label{fig:composite}
\end{figure}

\newpage
\section*{Conclusion}

This report successfully implemented fundamental 2D geometric transformations using homogeneous coordinate systems and matrix operations. The transformations demonstrated include:

\begin{itemize}
    \item \textbf{Translation:} Position changes without deformation
    \item \textbf{Rotation:} Angular displacement preserving distances
    \item \textbf{Scaling:} Size modifications with aspect ratio control
    \item \textbf{Reflection:} Mirror imaging across axes
    \item \textbf{Shearing:} Affine distortions maintaining parallelism
    \item \textbf{Composite Transformations:} Complex operations through matrix composition
\end{itemize}

Homogeneous coordinates provide a unified mathematical framework for all transformations, enabling efficient computation and hardware acceleration. These fundamental operations form the basis for computer graphics, animation, CAD systems, and image processing applications.

\end{document}