def check_safe(report):
    levels = [int(level) for level in report.split()]

    is_increasing = levels[0] < levels[1]
    is_decreasing = levels[0] > levels[1]

    if not (is_increasing or is_decreasing):
        return 0

    for i in range(len(levels) - 1):
        current, next = levels[i], levels[i + 1]

        if not (1 <= abs(current - next) <= 3):
            return 0

        match (is_increasing, is_decreasing):
            case (True, False):
                if next <= current:
                    return 0
            case (False, True):
                if next >= current:
                    return 0

    return 1


with open("../inputs/day2.txt") as f:
    reports = f.readlines()

total = sum(check_safe(report) for report in reports)

print("Task 1:", total)


def check_safe_v2(report):
    levels = [int(level) for level in report.split()]

    def is_strictly_increasing_with_one_removal(levels):
        errors = 0
        for i in range(len(levels) - 1):
            if levels[i] >= levels[i + 1]:
                if errors == 1:
                    return False
                errors += 1
                # Skip the current or next number and continue checking
                if i > 0 and levels[i - 1] >= levels[i + 1]:
                    levels[i + 1] = levels[i]
        return True

    def is_strictly_decreasing_with_one_removal(levels):
        errors = 0
        for i in range(len(levels) - 1):
            if levels[i] <= levels[i + 1]:
                if errors == 1:
                    return False
                errors += 1
                # Skip the current or next number and continue checking
                if i > 0 and levels[i - 1] <= levels[i + 1]:
                    levels[i + 1] = levels[i]
        return True

    if not (
        is_strictly_increasing_with_one_removal(levels[:])
        or is_strictly_decreasing_with_one_removal(levels[:])
    ):
        return 0

    errors = 0
    i = 0

    while i < len(levels) - 1:
        current, next = levels[i], levels[i + 1]

        if not (1 <= abs(current - next) <= 3):
            if errors == 1:
                return 0
            errors += 1
            i += 1
            continue

        i += 1

    return 1


total = sum(check_safe_v2(report) for report in reports)

print("Task 2:", total)
