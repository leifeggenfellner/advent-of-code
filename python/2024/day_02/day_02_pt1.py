from utils import is_safe


def part_1_solve(input_data):
    def check_safe(report):
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            return 1

        return 0

    return sum(check_safe(report) for report in input_data)
