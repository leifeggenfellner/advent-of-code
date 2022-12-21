def process_part1(data: str) -> int:
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i
    return -1


def process_part2(data: str) -> int:
    for i in range(15, len(data)):
        if len(set(data[i-14:i])) == 14:
            return i
    return -1
