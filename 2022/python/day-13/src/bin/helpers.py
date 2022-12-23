def compare_values(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return a - b
        elif type(b) == list:
            return compare_values([a], b)
    else:
        if isinstance(b, int):
            return compare_values(a, [b])

    for x, y in zip(a, b):
        value = compare_values(x, y)
        if value:
            return value

    return len(a) - len(b)


def process_part1(data: str) -> int:
    pairs = list(map(str.splitlines, data.strip().split("\n\n")))
    sum_of_indices = 0

    for i, (el1, el2) in enumerate(pairs):
        if compare_values(eval(el1), eval(el2)) < 0:
            sum_of_indices += i + 1

    return sum_of_indices


def process_part2(data: str) -> int:
    from functools import cmp_to_key
    pairs = list(map(eval, data.split())) + [[[2]], [[6]]]
    pairs.sort(key=cmp_to_key(compare_values))
    return (pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1)
