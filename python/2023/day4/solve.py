with open("input.txt", "r") as f:
    cards = [line.replace("  ", " ").strip() for line in f.readlines()]

# Part 1

total = 0

for card in cards:
    numbers = card.split(":")[1].strip().split(" | ")
    winning_numbers = set(numbers[0].split(" "))
    your_numbers = set(numbers[1].split(" "))

    matching_numbers = winning_numbers.intersection(your_numbers)

    if len(matching_numbers) > 0:
        total += 1 << len(matching_numbers) - 1


print(total)

# Part 2


total_cards = [1] * len(cards)

for card in cards:
    parts = card.split(":")
    game_number = int(parts[0].split()[1]) - 1
    numbers = parts[1].strip().split(" | ")
    winning_numbers = set(numbers[0].split())
    your_numbers = set(numbers[1].split())

    matching_numbers = winning_numbers.intersection(your_numbers)

    for i in range(1, len(matching_numbers) + 1):
        if game_number + i < len(total_cards):
            total_cards[game_number + i] += total_cards[game_number]


print(sum(total_cards))
