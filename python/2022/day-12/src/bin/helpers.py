def process_part1(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]

    for row, line in enumerate(grid):
        for column, letter in enumerate(line):
            if letter == "S":
                start_row = row
                start_column = column
                grid[row][column] = "a"
            elif letter == "E":
                end_row = row
                end_column = column
                grid[row][column] = "z"

    queue = []
    queue.append((0, start_row, start_column))

    visited = {(start_row, start_column)}

    while queue:
        distance, row, column = queue.pop(0)
        for next_row, next_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
            if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[0]):
                continue
            elif (next_row, next_column) in visited:
                continue
            elif ord(grid[next_row][next_column]) - ord(grid[row][column]) > 1:
                continue
            elif next_row == end_row and next_column == end_column:
                return distance + 1

            visited.add((next_row, next_column))
            queue.append((distance + 1, next_row, next_column))

    return -1


def process_part2(data: str) -> int:
    grid = [list(row) for row in data.splitlines()]

    for row, line in enumerate(grid):
        for column, letter in enumerate(line):
            if letter == "S":
                grid[row][column] = "a"
            elif letter == "E":
                end_row = row
                end_column = column
                grid[row][column] = "z"

    queue = []
    queue.append((0, end_row, end_column))

    visited = {(end_row, end_column)}

    while queue:
        distance, row, column = queue.pop(0)
        for next_row, next_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
            if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[0]):
                continue
            elif (next_row, next_column) in visited:
                continue
            elif ord(grid[next_row][next_column]) - ord(grid[row][column]) < -1:
                continue
            elif grid[next_row][next_column] == "a":
                return distance + 1

            visited.add((next_row, next_column))
            queue.append((distance + 1, next_row, next_column))

    return -1
