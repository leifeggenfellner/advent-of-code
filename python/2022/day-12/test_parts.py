from src.bin.helpers import process_part1, process_part2

INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def test_part1():
    assert process_part1(INPUT) == 31


def test_part2():
    assert process_part2(INPUT) == 29
