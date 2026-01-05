from src.bin.helpers import process_part1, process_part2

INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_part1():
    assert process_part1(INPUT) == 2


def test_part2():
    assert process_part2(INPUT) == 4
