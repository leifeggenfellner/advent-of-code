from src.bin.helpers import process_part1, process_part2

INPUT = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def test_part1():
    assert process_part1(INPUT) == 24


def test_part2():
    assert process_part2(INPUT) == 93
