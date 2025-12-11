"""
Maze representation module.

This module provides the Maze class for representing and working with mazes.
"""


class Maze:
    """
    Represents a 2D maze grid.
    
    The maze is represented as a 2D list where:
    - 0 represents a path (walkable)
    - 1 represents a wall (not walkable)
    - 'S' represents the start position
    - 'E' represents the end/goal position
    """
    
    def __init__(self, grid):
        """
        Initialize the maze with a grid.
        
        Args:
            grid: A 2D list representing the maze layout
        """
        self.grid = grid
        self.rows = len(grid)
        # Validate that all rows have the same length
        self.cols = len(grid[0]) if grid else 0
        for i, row in enumerate(grid):
            if len(row) != self.cols:
                raise ValueError(f"Row {i} has length {len(row)}, expected {self.cols}")
        self.start = self._find_position('S')
        self.end = self._find_position('E')
        
    def _find_position(self, marker):
        """
        Find the position of a marker in the maze.
        
        Args:
            marker: The marker to search for ('S' or 'E')
            
        Returns:
            Tuple (row, col) if found, None otherwise
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == marker:
                    return (i, j)
        return None
    
    def is_valid_position(self, row, col):
        """
        Check if a position is valid and walkable.
        
        Args:
            row: Row index
            col: Column index
            
        Returns:
            True if the position is within bounds and not a wall
        """
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        return self.grid[row][col] != 1
    
    def get_neighbors(self, row, col):
        """
        Get valid neighboring positions (up, down, left, right).
        
        Args:
            row: Current row
            col: Current column
            
        Returns:
            List of valid neighbor positions as (row, col) tuples
        """
        neighbors = []
        # Define movement directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def display(self, path=None):
        """
        Display the maze in a readable format.
        
        Args:
            path: Optional list of (row, col) tuples representing the solution path
        """
        path_set = set(path) if path else set()
        
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in path_set and self.grid[i][j] not in ['S', 'E']:
                    print('*', end=' ')  # Mark path with *
                elif self.grid[i][j] == 1:
                    print('█', end=' ')  # Wall
                elif self.grid[i][j] == 'S':
                    print('S', end=' ')  # Start
                elif self.grid[i][j] == 'E':
                    print('E', end=' ')  # End
                else:
                    print('.', end=' ')  # Empty path
            print()  # New line after each row
