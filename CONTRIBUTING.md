# Contributing to Maze Solver

Thank you for your interest in contributing. This guide will help you get started.

## First Time Contributing?

Welcome. If you're new to open source, this is a great place to start.

### Quick Start for Beginners

1. **Learn the basics**: Read the README.md to understand what the project does
2. **Run the code**: Execute `python main.py` to see it in action
3. **Pick a task**: Check the "Good First Issues" below
4. **Ask questions**: Don't hesitate to ask if something is unclear

## Good First Issues

These are suitable for newcomers:

### 1. Add a New Example Maze
**Difficulty**: Easy

Edit `example_mazes.py` and add a new function:

```python
def get_my_maze():
    """
    Returns a custom maze - describe it here!
    """
    return [
        ['S', 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 'E']
    ]
```

Then add it to the `MAZE_EXAMPLES` dictionary.

### 2. Improve Documentation
**Difficulty**: Easy

Add more comments explaining how the code works. Look for sections that could be clearer.

### 3. Add Input Validation
**Difficulty**: Medium

Add checks to ensure:
- Mazes have exactly one Start and one End
- All rows have the same length
- Only valid characters (0, 1, 'S', 'E') are used

### 4. Implement BFS Solver
**Difficulty**: Advanced

Create `bfs_solver.py` similar to `dfs_solver.py` but using Breadth-First Search instead. BFS uses a queue and finds the shortest path.

## Development Workflow

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/maze_solver.git
cd maze_solver
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Use prefixes like:
- `feature/` for new features
- `bugfix/` for bug fixes
- `docs/` for documentation
- `refactor/` for code improvements

### 3. Make Your Changes

- Write clean, readable code
- Add comments for complex logic
- Test your changes thoroughly

### 4. Test Your Code

```bash
python main.py
```

Make sure:
- The program runs without errors
- Your changes work as expected
- You didn't break existing functionality

### 5. Commit Your Changes

```bash
git add .
git commit -m "Add: brief description of your changes"
```

Good commit messages:
- `Add: new spiral maze example`
- `Fix: handle empty maze edge case`
- `Docs: explain DFS algorithm in README`
- `Refactor: simplify neighbor calculation`

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then go to GitHub and create a Pull Request.

## Code Style Guidelines

### Python Style (PEP 8)

```python
# Good variable names
path_length = 10
is_valid = True

# Bad variable names
x = 10
flag = True

# Good function with docstring
def calculate_distance(point1, point2):
    """
    Calculate Euclidean distance between two points.
    
    Args:
        point1: Tuple of (x, y) coordinates
        point2: Tuple of (x, y) coordinates
        
    Returns:
        Float representing the distance
    """
    # Implementation here
    pass

# Good spacing
def solve_maze(maze):
    if not maze:
        return None
    
    result = dfs_search(maze)
    return result
```

### Documentation

- Add docstrings to all functions and classes
- Explain **why**, not just **what**
- Use examples when helpful

### Comments

```python
# Good comment - explains WHY
# We use DFS because it uses less memory than BFS for deep mazes

# Bad comment - just repeats code
# Set x to 5
x = 5
```

## What to Contribute

### Easy Contributions
- Fix typos in documentation
- Add more example mazes
- Improve code comments
- Add error messages

### Medium Contributions
- Add input validation
- Create utility functions
- Add statistics/metrics
- Write tutorials

### Advanced Contributions
- Implement new algorithms (BFS, A*, Dijkstra)
- Add maze generation
- Create visualizations
- Performance optimizations
- Add GUI

## Pull Request Checklist

Before submitting, ensure:

- [ ] Code runs without errors
- [ ] Changes are tested
- [ ] Documentation is updated
- [ ] Code follows style guidelines
- [ ] Commit messages are clear
- [ ] PR description explains the changes

## Learning Resources

### Algorithms
- [Visualizing DFS](https://visualgo.net/en/dfsbfs)
- [Graph Algorithms Course](https://www.coursera.org/learn/algorithms-graphs-data-structures)

### Python
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python Tutorials](https://realpython.com/)

### Git & GitHub
- [GitHub Guides](https://guides.github.com/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

## Questions?

- **Code questions**: Open an issue with the "question" label
- **Bug reports**: Open an issue with the "bug" label
- **Feature ideas**: Open an issue with the "enhancement" label

## Code of Conduct

Be respectful and inclusive. We're all here to learn and help each other!

- Be kind and patient with newcomers
- Give constructive feedback
- Respect different skill levels
- Help others when you can

## Recognition

All contributors will be recognized. Your contributions help everyone learn.

Thank you for contributing to Maze Solver.
