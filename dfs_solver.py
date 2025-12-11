"""
DFS (Depth-First Search) Maze Solver.

This module implements the DFS algorithm to find a path through a maze.
DFS is a fundamental graph traversal algorithm that explores as far as possible
along each branch before backtracking.
"""


class DFSSolver:
    """
    Solves mazes using the Depth-First Search algorithm.
    
    DFS works by:
    1. Starting at the initial position
    2. Exploring each neighbor recursively
    3. Marking visited positions to avoid cycles
    4. Backtracking when a dead end is reached
    5. Returning the path when the goal is found
    """
    
    def __init__(self, maze):
        """
        Initialize the solver with a maze.
        
        Args:
            maze: A Maze object to solve
        """
        self.maze = maze
        self.visited = set()
        self.path = []
        
    def solve(self):
        """
        Solve the maze using DFS.
        
        Returns:
            List of (row, col) tuples representing the path from start to end,
            or None if no path exists
        """
        if not self.maze.start or not self.maze.end:
            print("Error: Maze must have both start (S) and end (E) positions")
            return None
        
        self.visited.clear()
        self.path.clear()
        
        if self._dfs(self.maze.start[0], self.maze.start[1]):
            return self.path.copy()
        else:
            return None
    
    def _dfs(self, row, col):
        """
        Recursive DFS helper function.
        
        Args:
            row: Current row position
            col: Current column position
            
        Returns:
            True if a path to the end is found, False otherwise
        """
        # Check if we've reached the goal
        if (row, col) == self.maze.end:
            self.path.append((row, col))
            return True
        
        # Mark current position as visited
        self.visited.add((row, col))
        self.path.append((row, col))
        
        # Explore all valid neighbors
        for neighbor_row, neighbor_col in self.maze.get_neighbors(row, col):
            # Skip if already visited
            if (neighbor_row, neighbor_col) in self.visited:
                continue
            
            # Recursively explore this neighbor
            if self._dfs(neighbor_row, neighbor_col):
                return True
        
        # Backtrack: remove current position from path if no solution found
        self.path.pop()
        return False
    
    def get_statistics(self):
        """
        Get statistics about the solving process.
        
        Returns:
            Dictionary with statistics (visited nodes, path length)
        """
        # Calculate efficiency only if we have both a path and visited nodes
        if self.visited and self.path:
            efficiency = len(self.path) / len(self.visited)
        else:
            efficiency = 0
        
        return {
            'visited_nodes': len(self.visited),
            'path_length': len(self.path),
            'efficiency': efficiency
        }
