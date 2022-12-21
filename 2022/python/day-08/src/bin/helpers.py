def process_part1(data: str) -> int:
    grid_map = [list(map(int, line)) for line in data.splitlines()]
    total = 0

    for row in range(len(grid_map)):
        for column in range(len(grid_map[row])):
            current_tile = grid_map[row][column]
            if all(grid_map[row][number] < current_tile for number in range(column)) or all(grid_map[row][number] < current_tile for number in range(column + 1, len(grid_map[row]))) or all(grid_map[number][column] < current_tile for number in range(row)) or all(grid_map[number][column] < current_tile for number in range(row + 1, len(grid_map))):
                total += 1
    return total


def process_part2(data: str) -> int:
    grid_map = [list(map(int, line)) for line in data.splitlines()]
    answer = 0

    for row in range(len(grid_map)):
        for column in range(len(grid_map[row])):
            current_tile = grid_map[row][column]
            up = down = left = right = 0
            for number in range(column - 1, -1, -1):
                left += 1
                if grid_map[row][number] >= current_tile:
                    break
            for number in range(column + 1, len(grid_map[row])):
                right += 1
                if grid_map[row][number] >= current_tile:
                    break
            for number in range(row - 1, -1, -1):
                up += 1
                if grid_map[number][column] >= current_tile:
                    break
            for number in range(row + 1, len(grid_map)):
                down += 1
                if grid_map[number][column] >= current_tile:
                    break

            if up * down * left * right > answer:
                answer = up * down * left * right

    return answer
