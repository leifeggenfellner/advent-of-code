def process_part1(data: str) -> int:
    visited = set([(0, 0)])
    head = [0, 0]
    tail = [0, 0]

    for line in data.splitlines():
        direction, steps = line.split()
        steps = int(steps)

        for _ in range(steps):
            move_x = 1 if direction == "R" else -1 if direction == "L" else 0
            move_y = 1 if direction == "U" else -1 if direction == "D" else 0

            head[0] += move_x
            head[1] += move_y

            delta_x = head[0] - tail[0]
            delta_y = head[1] - tail[1]

            if abs(delta_x) > 1 or abs(delta_y) > 1:
                if delta_x == 0:
                    tail[1] += delta_y // 2
                elif delta_y == 0:
                    tail[0] += delta_x // 2
                else:
                    tail[0] += 1 if delta_x > 0 else -1
                    tail[1] += 1 if delta_y > 0 else -1

            visited.add(tuple(tail))

    return len(visited)


def process_part2(data: str) -> int:
    visited = set([(0, 0)])
    rope = [[0, 0] for _ in range(10)]

    for line in data.splitlines():
        direction, steps = line.split()
        steps = int(steps)

        for _ in range(steps):
            move_x = 1 if direction == "R" else -1 if direction == "L" else 0
            move_y = 1 if direction == "U" else -1 if direction == "D" else 0

            rope[0][0] += move_x
            rope[0][1] += move_y

            for i in range(9):
                head = rope[i]
                tail = rope[i + 1]

                delta_x = head[0] - tail[0]
                delta_y = head[1] - tail[1]

                if abs(delta_x) > 1 or abs(delta_y) > 1:
                    if delta_x == 0:
                        tail[1] += delta_y // 2
                    elif delta_y == 0:
                        tail[0] += delta_x // 2
                    else:
                        tail[0] += 1 if delta_x > 0 else -1
                        tail[1] += 1 if delta_y > 0 else -1

            visited.add(tuple(rope[-1]))

    return len(visited)
