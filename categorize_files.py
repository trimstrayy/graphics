#!/usr/bin/env python3
"""
File categorization script for Computer Graphics assignments
"""

import os
import glob
from pathlib import Path

def categorize_files():
    """Categorize all files in the workspace by assignment type"""

    categories = {
        "Line Drawing Algorithms": {
            "files": ["bresenham_line.py", "dda_line.py"],
            "description": "Basic raster graphics line drawing algorithms"
        },
        "Circle/Ellipse Algorithms": {
            "files": ["midpoint_circle.py", "midpoint_ellipse.py"],
            "description": "Midpoint algorithms for curved shapes"
        },
        "2D Transformations": {
            "files": ["transformations.py", "main_transformations.py", "test_transformations.py", "README_transformations.md"],
            "directories": ["plots"],
            "description": "Complete 2D transformation system with homogeneous coordinates"
        },
        "Data Visualization": {
            "files": ["line_graph.py", "pie_chart.py"],
            "description": "Chart and graph plotting implementations"
        },
        "Operating System Simulation": {
            "directories": ["bhasmOS", "os-sandbox"],
            "description": "Web-based operating system simulator"
        },
        "Documentation": {
            "files": ["lab_report.md", "task.md", "requirements.txt", "README_transformations.md", "ASSIGNMENT_CATEGORIES.md"],
            "description": "Reports, requirements, and documentation files"
        },
        "Utilities": {
            "files": ["main.py", "name.py"],
            "description": "General utility and main program files"
        }
    }

    print("📊 COMPUTER GRAPHICS ASSIGNMENTS - FILE CATEGORIZATION")
    print("=" * 60)

    total_files = 0
    total_dirs = 0

    for category, info in categories.items():
        print(f"\n🔹 {category}")
        print(f"   {info['description']}")
        print("   " + "-" * 50)

        # Count files in this category
        cat_files = 0
        cat_dirs = 0

        # Check files
        if 'files' in info:
            for file in info['files']:
                if os.path.exists(file):
                    print(f"   📄 {file}")
                    cat_files += 1
                else:
                    print(f"   ⚠️  {file} (missing)")

        # Check directories
        if 'directories' in info:
            for dir_name in info['directories']:
                if os.path.exists(dir_name):
                    print(f"   📁 {dir_name}/")
                    cat_dirs += 1
                    # Count files in directory
                    try:
                        dir_files = len([f for f in Path(dir_name).rglob('*') if f.is_file()])
                        print(f"      └─ Contains {dir_files} files")
                        cat_files += dir_files
                    except:
                        pass
                else:
                    print(f"   ⚠️  {dir_name}/ (missing)")

        print(f"   📊 Category total: {cat_files} files, {cat_dirs} directories")
        total_files += cat_files
        total_dirs += cat_dirs

    print("\n" + "=" * 60)
    print(f"📈 WORKSPACE SUMMARY")
    print(f"   Total categorized files: {total_files}")
    print(f"   Total categorized directories: {total_dirs}")
    print(f"   Total assignment categories: {len(categories)}")

    # Check for uncategorized files
    all_files = []
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', '.git']]
        for file in files:
            if not file.startswith('.'):
                all_files.append(os.path.join(root, file))

    categorized_files = set()
    for cat_info in categories.values():
        if 'files' in cat_info:
            categorized_files.update(cat_info['files'])
        if 'directories' in cat_info:
            for dir_name in cat_info['directories']:
                try:
                    for file_path in Path(dir_name).rglob('*'):
                        if file_path.is_file():
                            categorized_files.add(str(file_path))
                except:
                    pass

    uncategorized = []
    for file_path in all_files:
        rel_path = os.path.relpath(file_path)
        if rel_path not in categorized_files and not any(rel_path.startswith(d + os.sep) for d in ['.git', '__pycache__', 'node_modules']):
            uncategorized.append(rel_path)

    if uncategorized:
        print(f"\n⚠️  Uncategorize files ({len(uncategorized)}):")
        for file in sorted(uncategorized)[:10]:  # Show first 10
            print(f"   • {file}")
        if len(uncategorized) > 10:
            print(f"   ... and {len(uncategorized) - 10} more")

if __name__ == "__main__":
    categorize_files()