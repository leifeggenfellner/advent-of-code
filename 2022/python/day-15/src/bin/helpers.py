def process_part1(data: str) -> int:
    import re
    pattern = re.compile(r"-?\d+")

    Y = 10

    known_beacons = set()
    invalid_locations = set()

    intervals = []

    for line in data.splitlines():
        sensor_x, sensor_y, beacon_x, beacon_y = map(
            int, pattern.findall(line))

        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        offset = distance - abs(sensor_y - Y)

        if offset < 0:
            continue

        low_x = sensor_x - offset
        high_x = sensor_x + offset

        intervals.append((low_x, high_x))

        if beacon_y == Y:
            known_beacons.add(beacon_x)

    intervals.sort()

    non_overlapping_intervals = []

    for low, high in intervals:
        if not non_overlapping_intervals:
            non_overlapping_intervals.append([low, high])
            continue

        non_overlapping_low, non_overlapping_high = non_overlapping_intervals[-1]

        if low >= non_overlapping_high:
            non_overlapping_intervals.append([low, high])
            continue

        non_overlapping_intervals[-1][1] = max(high, non_overlapping_high)

    for low, high in non_overlapping_intervals:
        for x in range(low, high + 1):
            invalid_locations.add(x)

    return len(invalid_locations - known_beacons)


def process_part2(data: str) -> int:
    import re

    pattern = re.compile(r"-?\d+")

    lines = [list(map(int, pattern.findall(line)))
             for line in data.splitlines()]

    search_boundry = 4_000_000

    for Y in range(search_boundry + 1):
        intervals = []

        for sensor_x, sensor_y, beacon_x, beacon_y in lines:
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            offset = distance - abs(sensor_y - Y)

            if offset < 0:
                continue

            low_x = sensor_x - offset
            high_x = sensor_x + offset

            intervals.append((low_x, high_x))

        intervals.sort()

        non_overlapping_intervals = []

        for low, high in intervals:
            if not non_overlapping_intervals:
                non_overlapping_intervals.append([low, high])
                continue

            non_overlapping_intervals_low, non_overlapping_intervals_high = non_overlapping_intervals[-1]

            if low > non_overlapping_intervals_high + 1:
                non_overlapping_intervals.append([low, high])
                continue

            non_overlapping_intervals[-1][1] = max(
                non_overlapping_intervals_high, high)

        x = 0
        for low, high in non_overlapping_intervals:
            if x < low:
                return x * 4000000 + Y
            x = max(x, high + 1)
            if x > search_boundry:
                break
