with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

# Part 1

num_of_cubes = {"red": 12, "green": 13, "blue": 14}

valid_games = []

for game in data:
    id = int(game.split(":")[0].replace("Game ", ""))

    red = 0
    green = 0
    blue = 0

    for cubes in game.split(": ")[1].split("; "):
        for cube in cubes.split(", "):
            color = cube.split(" ")[1]
            count = int(cube.split(" ")[0])

            if color == "red" and count > red:
                red = count
            elif color == "green" and count > green:
                green = count
            elif color == "blue" and count > blue:
                blue = count

    if (
        red <= num_of_cubes["red"]
        and green <= num_of_cubes["green"]
        and blue <= num_of_cubes["blue"]
    ):
        valid_games.append(id)

print(sum(valid_games))

# Part 2

total = 0

for game in data:
    id = int(game.split(":")[0].replace("Game ", ""))

    red = 0
    green = 0
    blue = 0

    for cubes in game.split(": ")[1].split("; "):
        for cube in cubes.split(", "):
            color = cube.split(" ")[1]
            count = int(cube.split(" ")[0])

            if color == "red" and count > red:
                red = count
            elif color == "green" and count > green:
                green = count
            elif color == "blue" and count > blue:
                blue = count

    total += red * green * blue
    print(red, green, blue)

print(total)
