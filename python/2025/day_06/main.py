from pathlib import Path

from part1 import part1
from part2 import part2


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "day_06.in"

def read_input():
    data = INPUT_FILE.read_text().splitlines()

    nums = [list(map(int, line.split())) for line in data[:-1]]
    operators = list(op.strip() for op in data[-1].split())

    return data, nums, operators

def main():
    data, nums, operators = read_input()
  
    result1 = part1(nums, operators)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()