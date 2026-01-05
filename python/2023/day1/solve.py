import re

with open("input.txt", "r") as f:
    data = [line.strip("\n") for line in f.readlines()]

# Part 1

subs = [re.sub("[^0-9]", "", line) for line in data]

print(sum(int(line[0] + line[-1]) for line in subs))

# Part 2

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sums = []

for line in data:
    string = ""
    final_str = ""

    left = 0

    for i, char in enumerate(line):
        string += char
        if char.isdigit():
            final_str += char

        for key, value in digit_map.items():
            if key in string[left : i + 1]:
                final_str += value
                left = i

    sums.append(int(final_str[0] + final_str[-1]))


print(sum(sums))
