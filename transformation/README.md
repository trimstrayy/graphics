# 2D Transformations - OpenGL Implementation

This directory contains OpenGL-based implementations of 2D geometric transformations.

## 📄 Programs

### Individual Transformations
- **`translation_2d.py`** - Interactive 2D translation with keyboard controls
- **`rotation_2d.py`** - Interactive 2D rotation around center point
- **`scaling_2d.py`** - Interactive 2D scaling with independent X/Y factors
- **`reflection_2d.py`** - 2D reflection across X-axis, Y-axis, and origin
- **`shearing_2d.py`** - Interactive 2D shearing in X and Y directions

### Composite Transformations
- **`composite_transformations.py`** - Multiple transformations combined

## 🚀 Running the Programs

Each program can be run independently:

```bash
cd transformation
python translation_2d.py
python rotation_2d.py
python scaling_2d.py
python reflection_2d.py
python shearing_2d.py
python composite_transformations.py
```

## 🎮 Controls

### Translation (translation_2d.py)
- **WASD**: Move translation vector
- **R**: Reset to default values
- **Q/ESC**: Quit

### Rotation (rotation_2d.py)
- **Q**: Rotate clockwise
- **E**: Rotate counter-clockwise
- **R**: Reset to 30 degrees
- **Space**: Reset to 0 degrees
- **ESC**: Quit

### Scaling (scaling_2d.py)
- **WASD**: Adjust X/Y scaling factors
- **Q**: Increase both factors
- **E**: Decrease both factors
- **R**: Reset to sx=1.5, sy=0.8
- **Space**: Reset to sx=1.0, sy=1.0
- **ESC**: Quit

### Reflection (reflection_2d.py)
- **1**: Reflect across X-axis
- **2**: Reflect across Y-axis
- **3**: Reflect through origin
- **R**: Reset to X-axis reflection
- **ESC**: Quit

### Shearing (shearing_2d.py)
- **WASD**: Adjust shearing factors
- **Q**: Reset X-shearing to 0
- **E**: Reset Y-shearing to 0
- **R**: Reset to shx=0.3, shy=0.2
- **Space**: Reset to no shearing
- **ESC**: Quit

### Composite (composite_transformations.py)
- **1-5**: Switch between different composite modes
- **R**: Reset to mode 1
- **ESC**: Quit

## 📋 Requirements

- Python 3.x
- PyOpenGL
- GLUT (FreeGLUT)

Install requirements:
```bash
pip install PyOpenGL PyOpenGL_accelerate
```

## 🎯 Features

- **Interactive Controls**: Real-time parameter adjustment
- **Visual Feedback**: Original vs transformed shapes
- **Multiple Shapes**: Triangle and rectangle demonstrations
- **Homogeneous Coordinates**: Proper mathematical implementation
- **OpenGL Rendering**: Hardware-accelerated graphics

## 📚 Mathematical Foundation

All transformations use homogeneous coordinate systems where 2D points (x, y) are represented as 3D vectors (x, y, 1). This allows all transformations to be represented as 3×3 matrices.

### Transformation Matrices

- **Translation**: `[1 0 tx; 0 1 ty; 0 0 1]`
- **Rotation**: `[cosθ -sinθ 0; sinθ cosθ 0; 0 0 1]`
- **Scaling**: `[sx 0 0; 0 sy 0; 0 0 1]`
- **Reflection X**: `[1 0 0; 0 -1 0; 0 0 1]`
- **Reflection Y**: `[-1 0 0; 0 1 0; 0 0 1]`
- **Shearing X**: `[1 sh 0; 0 1 0; 0 0 1]`

---
*Part of Computer Graphics Assignments - 5th Semester*</content>
<parameter name="filePath">d:\KU\5th SEMESTER\graphics\transformation\README.md