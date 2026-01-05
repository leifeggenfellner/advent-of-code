from pathlib import Path

from part1 import part1
from part2 import part2


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "day_01.in"


def read_input():
    return INPUT_FILE.read_text().splitlines()


def main():
    moves = read_input()

    print(f"Part 1: {part1(moves)}")
    print(f"Part 2: {part2(moves)}")


if __name__ == "__main__":
    main()
