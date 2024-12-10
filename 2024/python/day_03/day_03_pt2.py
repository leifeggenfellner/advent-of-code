import re


def extract_numbers(match):
    if match.startswith("mul"):
        return list(map(int, match[4:-1].split(",")))
    elif match.startswith("don't"):
        return 0
    elif match.startswith("do"):
        return 1


def part_2_solve(input_data):
    regex = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"

    mul_active = 1
    total = 0

    for line in input_data:
        matches = re.findall(regex, line)
        for match in matches:
            numbers = extract_numbers(match)
            if numbers == 0:
                mul_active = 0
            elif numbers == 1:
                mul_active = 1
            elif mul_active:
                total += numbers[0] * numbers[1]

    return total
