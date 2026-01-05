def process_part1(inventories: str) -> int:
    data = [calories.split('\n') for calories in inventories.split('\n\n')]
    data = [list(map(int, value)) for value in data]

    return max(sum(calorieList) for calorieList in data)


def process_part2(inventories: str) -> int:
    data = [calories.split('\n') for calories in inventories.split('\n\n')]
    data = [list(map(int, value)) for value in data]

    return sum(sorted(sum(calorieList) for calorieList in data)[-3:])
