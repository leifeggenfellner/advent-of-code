import re


def extract_numbers(match):
    return list(map(int, match[4:-1].split(",")))


def part_1_solve(input_data):
    regex = r"mul\(\d+,\d+\)"

    total = sum(
        numbers[0] * numbers[1]
        for line in input_data
        for match in re.findall(regex, line)
        for numbers in [extract_numbers(match)]
    )

    return total
