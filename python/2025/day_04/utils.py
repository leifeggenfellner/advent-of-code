def is_accessible(grid: list[list[str]], r: int, c: int) -> bool:
    """
    Check if a position in the grid is accessible based on surrounding '@' characters.

    A position is considered accessible if it has fewer than 4 adjacent '@' characters
    in all 8 directions (horizontal, vertical, and diagonal).

    Args:
        grid: A 2D grid represented as a list of strings, where each string is a row.
        r: The row index of the position to check.
        c: The column index of the position to check.

    Returns:
        bool: True if the position has fewer than 4 adjacent '@' characters, False otherwise.
    """
    rows = len(grid)
    cols = len(grid[0])

    return sum(
        grid[nr][nc] == "@"
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc)
        if 0 <= (nr := r + dr) < rows
        if 0 <= (nc := c + dc) < cols
    ) < 4
