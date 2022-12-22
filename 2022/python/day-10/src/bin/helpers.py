def process_part1(data: str) -> int:
    X = 1
    register_values = [0]

    for line in data.splitlines():
        if line[0] == "n":
            register_values.append(X)
        else:
            value = int(line.split()[1])
            register_values.append(X)
            register_values.append(X)
            X += value

    return sum(a * b for a, b in list(enumerate(register_values))[20::40])


def process_part2(data: str) -> int:
    X = 1
    register_values = []

    for line in data.splitlines():
        if line[0] == "n":
            register_values.append(X)
        else:
            value = int(line.split()[1])
            register_values.append(X)
            register_values.append(X)
            X += value

    image = ""

    for i in range(0, len(register_values), 40):
        for j in range(40):
            image += "#" if abs(register_values[i + j] - j) <= 1 else " "
        image += "\n"

    return image
