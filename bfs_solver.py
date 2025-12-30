"""
bfs_solver.py
=================

This module implements a Breadth-First Search (BFS) based maze solver.

BFS is a graph-traversal algorithm that explores neighbors level-by-level.
In a maze where each move has equal cost, BFS guarantees the SHORTEST path.

Author: <your-name>
"""

from collections import deque
from typing import List, Tuple, Optional


# Type alias for readability
Coordinate = Tuple[int, int]


def bfs_solve(
    maze: List[List[int]],
    start: Coordinate,
    end: Coordinate
) -> Optional[List[Coordinate]]:
    """
    Solve a maze using Breadth-First Search (BFS).

    Parameters
    ----------
    maze : List[List[int]]
        2D grid where:
        0 -> free path
        1 -> wall / blocked

    start : (row, col)
        Starting cell coordinates

    end : (row, col)
        Target / destination cell coordinates

    Returns
    -------
    List[(row, col)] OR None
        Returns the SHORTEST PATH from start to end
        as a list of cell coordinates in order.
        Returns None if NO PATH exists.

    Why BFS?
    --------
    BFS explores the maze level-by-level.
    This means the first time we reach the target,
    we are guaranteed it is via the shortest path.
    """

    rows = len(maze)
    cols = len(maze[0])

    # Visited matrix to prevent revisiting cells
    visited = [[False] * cols for _ in range(rows)]

    # Queue stores (current_position, path_taken)
    queue = deque([(start, [start])])

    visited[start[0]][start[1]] = True

    # Possible movement directions (Down, Up, Right, Left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        (r, c), path = queue.popleft()

        # If we reached the destination → return the path
        if (r, c) == end:
            return path

        # Explore all neighbors
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            # Check boundaries AND not visited AND not a wall
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and maze[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append(((nr, nc), path + [(nr, nc)]))

    # No path exists
    return None


if __name__ == "__main__":
    """
    Example usage — this block runs ONLY when the file
    is executed directly.

    You can modify this grid to test with different mazes.
    """

    example_maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
    ]

    start_pos = (0, 0)
    end_pos = (3, 4)

    path = bfs_solve(example_maze, start_pos, end_pos)

    if path:
        print("Shortest path found:")
        print(path)
    else:
        print("No path exists in the maze.")
