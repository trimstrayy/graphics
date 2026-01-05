import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

class Transform2D:
    """
    Class to handle 2D transformations using homogeneous coordinate system
    """
    
    def __init__(self):
        """Initialize with identity matrix"""
        self.identity = np.eye(3)
    
    @staticmethod
    def homogeneous_coords(vertices):
        """
        Convert 2D vertices to homogeneous coordinates (3D)
        
        Args:
            vertices: numpy array of shape (n, 2) representing 2D points
            
        Returns:
            numpy array of shape (n, 3) with homogeneous coordinates
        """
        ones = np.ones((vertices.shape[0], 1))
        return np.hstack([vertices, ones])
    
    @staticmethod
    def to_2d(homogeneous_coords):
        """
        Convert homogeneous coordinates back to 2D
        
        Args:
            homogeneous_coords: numpy array of shape (n, 3)
            
        Returns:
            numpy array of shape (n, 2) with 2D coordinates
        """
        return homogeneous_coords[:, :2]
    
    @staticmethod
    def translation(tx, ty):
        """
        Create translation matrix
        
        Args:
            tx: translation in x direction
            ty: translation in y direction
            
        Returns:
            3x3 translation matrix
        """
        return np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def rotation(angle, degrees=True):
        """
        Create rotation matrix
        
        Args:
            angle: rotation angle
            degrees: if True, angle is in degrees; if False, in radians
            
        Returns:
            3x3 rotation matrix
        """
        if degrees:
            angle = np.radians(angle)
        
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        
        return np.array([
            [cos_a, -sin_a, 0],
            [sin_a, cos_a, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def scaling(sx, sy):
        """
        Create scaling matrix
        
        Args:
            sx: scaling factor in x direction
            sy: scaling factor in y direction
            
        Returns:
            3x3 scaling matrix
        """
        return np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def reflection_x():
        """
        Create reflection matrix across x-axis
        
        Returns:
            3x3 reflection matrix (x-axis)
        """
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def reflection_y():
        """
        Create reflection matrix across y-axis
        
        Returns:
            3x3 reflection matrix (y-axis)
        """
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def reflection_origin():
        """
        Create reflection matrix through origin
        
        Returns:
            3x3 reflection matrix (through origin)
        """
        return np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def shearing_x(shear_factor):
        """
        Create shearing matrix in x direction
        
        Args:
            shear_factor: shearing factor for x
            
        Returns:
            3x3 shearing matrix (x direction)
        """
        return np.array([
            [1, shear_factor, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def shearing_y(shear_factor):
        """
        Create shearing matrix in y direction
        
        Args:
            shear_factor: shearing factor for y
            
        Returns:
            3x3 shearing matrix (y direction)
        """
        return np.array([
            [1, 0, 0],
            [shear_factor, 1, 0],
            [0, 0, 1]
        ], dtype=float)
    
    @staticmethod
    def apply_transformation(vertices, matrix):
        """
        Apply transformation matrix to vertices
        
        Args:
            vertices: numpy array of shape (n, 2) with 2D points
            matrix: 3x3 transformation matrix
            
        Returns:
            numpy array of shape (n, 2) with transformed vertices
        """
        homo_coords = Transform2D.homogeneous_coords(vertices)
        transformed = homo_coords @ matrix.T
        return Transform2D.to_2d(transformed)
    
    @staticmethod
    def composite_transformation(*matrices):
        """
        Combine multiple transformation matrices
        
        Args:
            *matrices: variable number of 3x3 transformation matrices
            
        Returns:
            3x3 composite transformation matrix
        """
        result = np.eye(3)
        for matrix in matrices:
            result = result @ matrix
        return result


class Shape2D:
    """
    Base class for 2D shapes
    """
    
    def __init__(self, vertices, name="Shape"):
        """
        Initialize shape with vertices
        
        Args:
            vertices: numpy array of shape (n, 2) with 2D points
            name: name of the shape
        """
        self.original_vertices = vertices.copy()
        self.current_vertices = vertices.copy()
        self.name = name
    
    def apply_transformation(self, matrix):
        """Apply transformation matrix to shape"""
        self.current_vertices = Transform2D.apply_transformation(
            self.current_vertices, matrix
        )
    
    def reset(self):
        """Reset to original vertices"""
        self.current_vertices = self.original_vertices.copy()
    
    def translate(self, tx, ty):
        """Apply translation"""
        matrix = Transform2D.translation(tx, ty)
        self.apply_transformation(matrix)
    
    def rotate(self, angle, degrees=True):
        """Apply rotation"""
        matrix = Transform2D.rotation(angle, degrees)
        self.apply_transformation(matrix)
    
    def scale(self, sx, sy):
        """Apply scaling"""
        matrix = Transform2D.scaling(sx, sy)
        self.apply_transformation(matrix)
    
    def reflect_x(self):
        """Apply reflection across x-axis"""
        matrix = Transform2D.reflection_x()
        self.apply_transformation(matrix)
    
    def reflect_y(self):
        """Apply reflection across y-axis"""
        matrix = Transform2D.reflection_y()
        self.apply_transformation(matrix)
    
    def reflect_origin(self):
        """Apply reflection through origin"""
        matrix = Transform2D.reflection_origin()
        self.apply_transformation(matrix)
    
    def shear_x(self, shear_factor):
        """Apply shearing in x direction"""
        matrix = Transform2D.shearing_x(shear_factor)
        self.apply_transformation(matrix)
    
    def shear_y(self, shear_factor):
        """Apply shearing in y direction"""
        matrix = Transform2D.shearing_y(shear_factor)
        self.apply_transformation(matrix)


class Rectangle(Shape2D):
    """Rectangle shape defined by width and height"""
    
    def __init__(self, x, y, width, height):
        """
        Initialize rectangle
        
        Args:
            x: x-coordinate of bottom-left corner
            y: y-coordinate of bottom-left corner
            width: width of rectangle
            height: height of rectangle
        """
        vertices = np.array([
            [x, y],
            [x + width, y],
            [x + width, y + height],
            [x, y + height]
        ], dtype=float)
        super().__init__(vertices, "Rectangle")


class Triangle(Shape2D):
    """Triangle shape defined by three vertices"""
    
    def __init__(self, p1, p2, p3):
        """
        Initialize triangle
        
        Args:
            p1, p2, p3: tuples or arrays representing triangle vertices
        """
        vertices = np.array([p1, p2, p3], dtype=float)
        super().__init__(vertices, "Triangle")


class Line(Shape2D):
    """Line shape defined by two points"""
    
    def __init__(self, p1, p2):
        """
        Initialize line
        
        Args:
            p1, p2: tuples or arrays representing line endpoints
        """
        vertices = np.array([p1, p2], dtype=float)
        super().__init__(vertices, "Line")


def plot_shapes(shapes_list, title="2D Transformations", grid=True):
    """
    Plot multiple shapes
    
    Args:
        shapes_list: list of Shape2D objects
        title: title of the plot
        grid: whether to show grid
    """
    plt.figure(figsize=(12, 8))
    
    colors = plt.cm.tab10(np.linspace(0, 1, len(shapes_list)))
    
    for shape, color in zip(shapes_list, colors):
        if len(shape.current_vertices) == 2:
            # Line
            plt.plot(shape.current_vertices[:, 0], 
                    shape.current_vertices[:, 1], 
                    'o-', linewidth=2, markersize=8,
                    label=shape.name, color=color)
        else:
            # Polygon (close the shape)
            vertices = np.vstack([shape.current_vertices, shape.current_vertices[0]])
            plt.plot(vertices[:, 0], vertices[:, 1], 'o-', linewidth=2, markersize=8,
                    label=shape.name, color=color)
            plt.fill(vertices[:, 0], vertices[:, 1], alpha=0.2, color=color)
    
    plt.grid(grid)
    plt.axis('equal')
    plt.legend(loc='best')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
