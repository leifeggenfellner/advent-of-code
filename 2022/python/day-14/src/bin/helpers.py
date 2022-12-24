def process_part1(data: str) -> int:
    blocked = set()
    abyss = 0

    for line in data.splitlines():
        coordinates = [list(map(int, pair.split(",")))
                       for pair in line.split(" -> ")]

        for (col1, row1), (col2, row2) in zip(coordinates, coordinates[1:]):
            col1, col2 = sorted([col1, col2])
            row1, row2 = sorted([row1, row2])

            for col in range(col1, col2 + 1):
                for row in range(row1, row2 + 1):
                    blocked.add(col + row * 1j)
                    abyss = max(abyss, row + 1)

    total = 0

    while True:
        start = 500

        while True:
            if start.imag >= abyss:
                return total
            if start + 1j not in blocked:
                start += 1j
                continue
            elif start + 1j - 1 not in blocked:
                start += 1j - 1
                continue
            elif start + 1j + 1 not in blocked:
                start += 1j + 1
                continue

            blocked.add(start)
            total += 1
            break


def process_part2(data: str) -> int:
    blocked = set()
    floor = 0

    for line in data.splitlines():
        coordinates = [list(map(int, pair.split(",")))
                       for pair in line.split(" -> ")]

        for (col1, row1), (col2, row2) in zip(coordinates, coordinates[1:]):
            col1, col2 = sorted([col1, col2])
            row1, row2 = sorted([row1, row2])

            for col in range(col1, col2 + 1):
                for row in range(row1, row2 + 1):
                    blocked.add(col + row * 1j)
                    floor = max(floor, row + 1)

    total = 0

    while 500 not in blocked:
        start = 500

        while True:
            if start.imag >= floor:
                break
            if start + 1j not in blocked:
                start += 1j
                continue
            elif start + 1j - 1 not in blocked:
                start += 1j - 1
                continue
            elif start + 1j + 1 not in blocked:
                start += 1j + 1
                continue
            break

        blocked.add(start)
        total += 1

    return total
