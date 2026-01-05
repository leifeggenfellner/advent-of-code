from utils import is_accessible

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def part2(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    frontier = {
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if grid[r][c] == "@"
    }

    while frontier:
        next_frontier = set()

        for r, c in frontier:
            if grid[r][c] == "@" and is_accessible(grid, r, c):
                grid[r][c] = "."
                total += 1

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        next_frontier.add((nr, nc))

        frontier = next_frontier

    return total
