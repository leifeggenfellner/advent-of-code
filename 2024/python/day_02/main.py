from day_02_pt1 import part_1_solve
from day_02_pt2 import part_2_solve


def main():
    with open("./day02.in") as f:
        input_data = f.readlines()

    part_1_result = part_1_solve(input_data)
    part_2_result = part_2_solve(input_data)

    print(f"Part 1: {part_1_result}")
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
