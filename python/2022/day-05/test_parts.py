from src.bin.helpers import process_part1, process_part2

MOVES = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_part1():
    CRATES = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]

    assert process_part1(CRATES, MOVES) == "CMZ"


def test_part2():
    CRATES = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]

    assert process_part2(CRATES, MOVES) == "MCD"
