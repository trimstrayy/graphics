# 2D Transformations Implementation

This project implements all fundamental 2D transformations using homogeneous coordinate systems as required for the graphics assignment.

## Features Implemented

### Basic Transformations
1. **2D Translation** - Move objects in the XY plane
2. **2D Rotation** - Rotate objects around the origin
3. **2D Scaling** - Scale objects in X and Y directions
4. **2D Reflection** - Reflect objects across X-axis, Y-axis, and through origin
5. **2D Shearing** - Shear objects in X and Y directions

### Composite Transformations
- Translation + Rotation
- Scaling + Reflection
- Rotation + Shearing
- Translation + Scaling + Rotation
- All transformations combined

## Files

- `transformations.py` - Core transformation classes and methods
- `main_transformations.py` - Main demonstration program
- `requirements.txt` - Python dependencies

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the main demonstration program:
```bash
python main_transformations.py
```

This will display multiple plots showing:
- Individual transformations on different shapes (Rectangle, Triangle, Line)
- Composite transformations combining multiple operations
- Matrix operations demonstration

## Classes Overview

### Transform2D
Core class containing static methods for:
- Converting between 2D and homogeneous coordinates
- Creating transformation matrices
- Applying transformations
- Composing multiple transformations

### Shape Classes
- `Rectangle` - Defined by position, width, and height
- `Triangle` - Defined by three vertices
- `Line` - Defined by two endpoints

All shapes support all transformation operations.

## Mathematical Foundation

All transformations use homogeneous coordinate systems where 2D points (x, y) are represented as 3D vectors (x, y, 1). This allows all transformations to be represented as 3×3 matrices and composed using matrix multiplication.

### Transformation Matrices

- **Translation**: `[1 0 tx; 0 1 ty; 0 0 1]`
- **Rotation**: `[cosθ -sinθ 0; sinθ cosθ 0; 0 0 1]`
- **Scaling**: `[sx 0 0; 0 sy 0; 0 0 1]`
- **Reflection X**: `[1 0 0; 0 -1 0; 0 0 1]`
- **Reflection Y**: `[-1 0 0; 0 1 0; 0 0 1]`
- **Shearing X**: `[1 sh 0; 0 1 0; 0 0 1]`

## Requirements Met

✅ 2D Translation
✅ 2D Rotation
✅ 2D Scaling
✅ 2D Reflection
✅ 2D Shearing
✅ Composite Transformations (5 different combinations)
✅ Homogeneous coordinate systems
✅ Multiple 2D shapes (Line, Triangle, Rectangle)

## Output

The program generates multiple matplotlib plots demonstrating each transformation type. Each plot shows how the transformations affect different geometric shapes.