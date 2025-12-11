"""
Main entry point for the Maze Solver application.

This script demonstrates how to use the DFS maze solver with example mazes.
"""

from maze import Maze
from dfs_solver import DFSSolver
from example_mazes import MAZE_EXAMPLES


def solve_and_display(maze_grid, maze_name):
    """
    Solve a maze and display the results.
    
    Args:
        maze_grid: 2D list representing the maze
        maze_name: Name of the maze for display purposes
    """
    print(f"\n{'='*60}")
    print(f"Solving: {maze_name.upper()} MAZE")
    print(f"{'='*60}")
    
    # Create maze object
    maze = Maze(maze_grid)
    
    print("\nOriginal Maze:")
    maze.display()
    
    # Create solver and solve
    solver = DFSSolver(maze)
    path = solver.solve()
    
    # Display results
    if path:
        print(f"\n✓ Solution found!")
        print(f"\nMaze with Solution Path (marked with *):")
        maze.display(path)
        
        # Display statistics
        stats = solver.get_statistics()
        print(f"\nStatistics:")
        print(f"  - Path length: {stats['path_length']} steps")
        print(f"  - Nodes visited: {stats['visited_nodes']}")
        print(f"  - Efficiency: {stats['efficiency']:.2%}")
    else:
        print(f"\n✗ No solution exists for this maze!")


def main():
    """
    Main function to run the maze solver demonstrations.
    """
    print("="*60)
    print("DFS MAZE SOLVER - Educational Implementation")
    print("="*60)
    print("\nThis program demonstrates the Depth-First Search (DFS)")
    print("algorithm for solving mazes.")
    print("\nLegend:")
    print("  S = Start position")
    print("  E = End/Goal position")
    print("  █ = Wall (impassable)")
    print("  . = Open path")
    print("  * = Solution path")
    
    # Solve all example mazes
    for name, maze_grid in MAZE_EXAMPLES.items():
        solve_and_display(maze_grid, name)
    
    print(f"\n{'='*60}")
    print("All demonstrations complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
