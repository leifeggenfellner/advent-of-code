from utils import is_safe


def part_2_solve(input_data):
    def check_safe(report):
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            return 1

        for i in range(len(levels)):
            levels_no_i = levels[:i] + levels[i + 1 :]
            if is_safe(levels_no_i):
                return 1

        return 0

    total = sum(check_safe(report) for report in input_data)

    return total
