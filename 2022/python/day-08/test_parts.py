from src.bin.helpers import process_part1, process_part2

INPUT = """30373
25512
65332
33549
35390
"""


def test_part1():
    assert process_part1(INPUT) == 21


def test_part2():
    assert process_part2(INPUT) == 8
