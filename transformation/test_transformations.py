#!/usr/bin/env python3
"""
Test script to verify 2D transformations implementation
"""

import numpy as np
from transformations import Transform2D, Rectangle, Triangle, Line

def test_homogeneous_coords():
    """Test homogeneous coordinate conversion"""
    print("Testing homogeneous coordinates...")

    vertices = np.array([[1, 2], [3, 4]])
    homo = Transform2D.homogeneous_coords(vertices)
    expected = np.array([[1, 2, 1], [3, 4, 1]])

    assert np.allclose(homo, expected), "Homogeneous conversion failed"
    print("✓ Homogeneous coordinates test passed")

def test_translation():
    """Test translation matrix"""
    print("Testing translation...")

    T = Transform2D.translation(2, 3)
    expected = np.array([[1, 0, 2], [0, 1, 3], [0, 0, 1]])

    assert np.allclose(T, expected), "Translation matrix incorrect"
    print("✓ Translation test passed")

def test_rotation():
    """Test rotation matrix"""
    print("Testing rotation...")

    R = Transform2D.rotation(90, degrees=True)
    expected = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

    assert np.allclose(R, expected), "Rotation matrix incorrect"
    print("✓ Rotation test passed")

def test_scaling():
    """Test scaling matrix"""
    print("Testing scaling...")

    S = Transform2D.scaling(2, 3)
    expected = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 1]])

    assert np.allclose(S, expected), "Scaling matrix incorrect"
    print("✓ Scaling test passed")

def test_composite():
    """Test composite transformations"""
    print("Testing composite transformations...")

    T = Transform2D.translation(1, 1)
    R = Transform2D.rotation(90, degrees=True)
    composite = Transform2D.composite_transformation(T, R)

    # Manual calculation: T * R
    expected = T @ R

    assert np.allclose(composite, expected), "Composite transformation incorrect"
    print("✓ Composite transformation test passed")

def test_shape_transformations():
    """Test shape transformation methods"""
    print("Testing shape transformations...")

    rect = Rectangle(0, 0, 2, 2)
    original = rect.current_vertices.copy()

    # Test translation
    rect.translate(1, 1)
    expected = original + np.array([1, 1])
    assert np.allclose(rect.current_vertices, expected), "Rectangle translation failed"

    # Test reset
    rect.reset()
    assert np.allclose(rect.current_vertices, original), "Rectangle reset failed"

    # Test scaling
    rect.scale(2, 2)
    expected = original * 2
    assert np.allclose(rect.current_vertices, expected), "Rectangle scaling failed"

    print("✓ Shape transformations test passed")

def test_apply_transformation():
    """Test transformation application"""
    print("Testing transformation application...")

    vertices = np.array([[1, 0], [0, 1]])
    T = Transform2D.translation(1, 1)

    result = Transform2D.apply_transformation(vertices, T)
    expected = np.array([[2, 1], [1, 2]])

    assert np.allclose(result, expected), "Apply transformation failed"
    print("✓ Apply transformation test passed")

def run_all_tests():
    """Run all test functions"""
    print("Running 2D Transformations Tests")
    print("=" * 35)

    try:
        test_homogeneous_coords()
        test_translation()
        test_rotation()
        test_scaling()
        test_composite()
        test_shape_transformations()
        test_apply_transformation()

        print("\n" + "=" * 35)
        print("ALL TESTS PASSED! ✓")
        print("2D Transformations implementation is correct.")
        print("=" * 35)

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        return False

    return True

if __name__ == "__main__":
    run_all_tests()