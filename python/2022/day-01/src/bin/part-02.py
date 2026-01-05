from helpers import process_part2
from pathlib import Path


def main():
    input_file = Path(__file__).parents[2] / "input.txt"
    data = input_file.read_text()
    print(process_part2(data))


if __name__ == "__main__":
    main()
