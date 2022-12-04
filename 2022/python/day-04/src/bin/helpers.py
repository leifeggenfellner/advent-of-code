def process_part1(pairs: str) -> int:
    lines = [pair.split(",") for pair in pairs.splitlines()]
    total = 0

    for line in lines:
        pair1, pair2 = zip(line[0].split("-"), line[1].split("-"))
        pair1Numbers = set(range(int(pair1[0]), int(pair1[1]) + 1))
        pair2Numbers = set(range(int(pair2[0]), int(pair2[1]) + 1))

        if pair1Numbers.issubset(pair2Numbers) or pair2Numbers.issubset(pair1Numbers):
            total += 1

    return total


def process_part2(pairs: str) -> int:
    lines = [pair.split(",") for pair in pairs.splitlines()]
    total = 0

    for line in lines:
        pair1, pair2 = zip(line[0].split("-"), line[1].split("-"))
        pair1Numbers = set(range(int(pair1[0]), int(pair1[1]) + 1))
        pair2Numbers = set(range(int(pair2[0]), int(pair2[1]) + 1))

        if pair1Numbers.intersection(pair2Numbers):
            total += 1

    return total
