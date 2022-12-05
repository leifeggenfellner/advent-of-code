from helpers import process_part1
from pathlib import Path


def main():
    CRATES = [
        ["N", "C", "R", "T", "M", "Z", "P"],
        ["D", "N", "T", "S", "B", "Z"],
        ["M", "H", "Q", "R", "F", "C", "T", "G"],
        ["G", "R", "Z"],
        ["Z", "N", "R", "H"],
        ["F", "H", "S", "W", "P", "Z", "L", "D"],
        ["W", "D", "Z", "R", "C", "G", "M"],
        ["S", "J", "F", "L", "H", "W", "Z", "Q"],
        ["S", "Q", "P", "W", "N"]
    ]

    input_file = Path(__file__).parents[2] / "input.txt"
    moves = input_file.read_text()

    print(process_part1(CRATES, moves))


if __name__ == "__main__":
    main()
