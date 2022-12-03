def process_part1(rucksacks: str) -> int:
    sorting_letters = [
        letter for rucksack in rucksacks.splitlines() for letter in set(rucksack) if letter in rucksack[:len(rucksack) // 2] and letter in rucksack[len(rucksack) // 2:]]
    return sum(ord(letter) - 96 if letter.islower() else ord(letter) - 38 for letter in sorting_letters)


def process_part2(rucksacks: str) -> int:
    from itertools import zip_longest
    args = [iter(rucksacks.splitlines())] * 3
    restructured_rucksacks = list(zip_longest(fillvalue='', *args))
    return sum(ord(letter) - 96 if letter.islower() else ord(letter) - 38 for rucksack in restructured_rucksacks for letter in set(rucksack[0]) if letter in rucksack[1] and letter in rucksack[2])
