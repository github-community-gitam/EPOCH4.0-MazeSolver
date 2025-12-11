"""
Example mazes for testing and learning.

This module provides pre-defined mazes of varying difficulty levels
for testing the DFS solver and learning purposes.
"""


def get_simple_maze():
    """
    Returns a simple 5x5 maze - great for beginners.
    
    Layout:
    S . . . .
    █ █ █ █ .
    . . . . .
    . █ █ █ █
    . . . . E
    """
    return [
        ['S', 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 'E']
    ]


def get_medium_maze():
    """
    Returns a medium complexity 8x8 maze.
    
    This maze has multiple dead ends and requires backtracking.
    """
    return [
        ['S', 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 'E']
    ]


def get_complex_maze():
    """
    Returns a complex 10x10 maze with many dead ends.
    
    This maze demonstrates DFS backtracking behavior well.
    """
    return [
        ['S', 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 'E']
    ]


def get_spiral_maze():
    """
    Returns a spiral-shaped maze - interesting for visualization.
    
    This maze creates a spiral path from start to end.
    """
    return [
        ['S', 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 'E']
    ]


def get_impossible_maze():
    """
    Returns an unsolvable maze - demonstrates that DFS correctly
    identifies when no solution exists.
    """
    return [
        ['S', 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 'E']
    ]


# Dictionary for easy access to all mazes
MAZE_EXAMPLES = {
    'simple': get_simple_maze(),
    'medium': get_medium_maze(),
    'complex': get_complex_maze(),
    'spiral': get_spiral_maze(),
    'impossible': get_impossible_maze()
}
