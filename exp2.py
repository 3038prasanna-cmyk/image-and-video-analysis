import numpy as np
import matplotlib.pyplot as plt

class QuadTreeNode:
    def __init__(self, x, y, size, value=None):
        self.x = x        # top-left x-coordinate
        self.y = y        # top-left y-coordinate
        self.size = size  # size of the square region
        self.value = value # None if not leaf, else 0 or 1
        self.children = []  # top-left, top-right, bottom-left, bottom-right

# Check if a region is homogeneous
def is_homogeneous(region):
    return np.all(region == region[0,0])

# Build quad tree recursively
def build_quadtree(image, x=0, y=0, size=None):
    if size is None:
        size = image.shape[0]

    region = image[y:y+size, x:x+size]

    if is_homogeneous(region):
        return QuadTreeNode(x, y, size, value=region[0,0])
    else:
        node = QuadTreeNode(x, y, size)
        half = size // 2
        node.children.append(build_quadtree(image, x, y, half))               # Top-left
        node.children.append(build_quadtree(image, x+half, y, half))          # Top-right
        node.children.append(build_quadtree(image, x, y+half, half))          # Bottom-left
        node.children.append(build_quadtree(image, x+half, y+half, half))     # Bottom-right
        return node

# Print quadtree
def print_quadtree(node, indent=0):
    if node.value is not None:
        print('  ' * indent + f'Leaf: value={node.value}, size={node.size}, pos=({node.x},{node.y})')
    else:
        print('  ' * indent + f'Node: size={node.size}, pos=({node.x},{node.y})')
        for child in node.children:
            print_quadtree(child, indent+1)

# Example binary image
image = np.array([
    [1,1,0,0],
    [1,1,0,0],
    [1,1,0,0],
    [1,1,0,0]
])

qt_root = build_quadtree(image)
print_quadtree(qt_root)
