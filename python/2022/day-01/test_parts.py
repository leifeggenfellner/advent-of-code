from src.bin.helpers import process_part1, process_part2

INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_part1():
    assert process_part1(INPUT) == 24000


def test_part2():
    assert process_part2(INPUT) == 45000
