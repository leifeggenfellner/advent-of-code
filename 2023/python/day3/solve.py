with open("input.txt", "r") as f:
    rows = [line.strip() for line in f.readlines()]

# Part 1

symbols = {"#", "$", "%", "&", "*", "+", "-", "/", "=", "@"}


def is_adjacent_to_symbol(r, c):
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(rows)
                and 0 <= nc < len(rows[0])
                and rows[nr][nc] in symbols
            ):
                return True
    return False


def find_next_number(row, start_col):
    while start_col < len(rows[row]) and not rows[row][start_col].isdigit():
        start_col += 1
    return start_col


total_sum = 0

for row in range(len(rows)):
    col = 0
    while col < len(rows[row]):
        if rows[row][col].isdigit():
            start_col = col
            number_str = ""

            adjacent_to_symbol = False
            while col < len(rows[row]) and rows[row][col].isdigit():
                number_str += rows[row][col]
                if not adjacent_to_symbol and is_adjacent_to_symbol(row, col):
                    adjacent_to_symbol = True
                col += 1

            if adjacent_to_symbol:
                total_sum += int(number_str)
        else:
            col = find_next_number(row, col + 1)

print(total_sum)


# Part 2


def find_part_numbers_around_gear(r, c):
    part_numbers = set()

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue

            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(rows)
                and 0 <= nc < len(rows[0])
                and rows[nr][nc].isdigit()
            ):
                number = ""
                while nc > 0 and rows[nr][nc - 1].isdigit():
                    nc -= 1
                while nc < len(rows[0]) and rows[nr][nc].isdigit():
                    number += rows[nr][nc]
                    nc += 1
                part_numbers.add(int(number))

    return list(part_numbers)


total_sum = 0

for row in range(len(rows)):
    for col in range(len(rows[0])):
        if rows[row][col] == "*":
            part_numbers = find_part_numbers_around_gear(row, col)
            if len(part_numbers) == 2:
                total_sum += part_numbers[0] * part_numbers[1]

print(total_sum)
