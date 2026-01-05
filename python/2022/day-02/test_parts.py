from src.bin.helpers import process_part1, process_part2

INPUT = """A Y
B X
C Z"""


def test_part1():
    assert process_part1(INPUT) == 15


def test_part2():
    assert process_part2(INPUT) == 12
