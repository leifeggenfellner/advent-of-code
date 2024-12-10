def is_safe(levels):
    if len(levels) < 2:
        return False

    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    if not (is_increasing or is_decreasing):
        return False

    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
