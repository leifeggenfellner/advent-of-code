from utils import is_accessible

def part1(grid: list[list[str]]) -> int:
    """
    Count the number of accessible positions marked with '@' in the grid.

    Args:
        grid (list[list[str]]): A 2D grid represented as a list of lists of strings, where each
                          string represents a row in the grid.

    Returns:
        int: The total count of accessible positions that contain the '@' character.
             For each '@' found in the grid, the accessibility is determined by
             calling is_accessible() with the grid and the position coordinates.
    """
    return sum(
        is_accessible(grid, r, c)
        for r in range(len(grid))
        for c in range(len(grid[r]))
        if grid[r][c] == "@"
    )
