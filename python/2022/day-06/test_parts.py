from src.bin.helpers import process_part1, process_part2

INPUT = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part1():
    assert process_part1(INPUT) == 7


def test_part2():
    assert process_part2(INPUT) == 19
