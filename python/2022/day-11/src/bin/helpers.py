def process_part1(data: str) -> int:
    monkeys = []

    for section in data.strip().split("\n\n"):
        lines = section.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)

    counters = [0] * len(monkeys)

    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item = int(item / 3)
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)

            counters[i] += len(monkey[0])
            monkey[0] = []

    counters.sort(reverse=True)

    return counters[0] * counters[1]


def process_part2(data: str) -> int:
    monkeys = []

    for section in data.strip().split("\n\n"):
        lines = section.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)

    counters = [0] * len(monkeys)

    modulo = 1
    for monkey in monkeys:
        modulo *= monkey[2]

    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= modulo
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)

            counters[i] += len(monkey[0])
            monkey[0] = []

    counters.sort(reverse=True)

    return counters[0] * counters[1]
