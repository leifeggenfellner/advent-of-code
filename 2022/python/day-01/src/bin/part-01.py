from helpers import process_part1


def main():
    with open("./input.txt") as f:
        data = f.read()

    print(process_part1(data))


if __name__ == "__main__":
    main()
