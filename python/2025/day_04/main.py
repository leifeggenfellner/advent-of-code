from pathlib import Path

from part1 import part1
from part2 import part2


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "day_04.in"


def read_input():
    return INPUT_FILE.read_text().splitlines()

def main():
    grid = [list(line) for line in read_input()]
  
    result1 = part1(grid)
    print(f"Part 1: {result1}")
    
    result2 = part2(grid)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()