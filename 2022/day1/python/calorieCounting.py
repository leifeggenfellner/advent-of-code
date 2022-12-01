with open('../input.txt', 'r') as f:
    data = [calories.split('\n') for calories in f.read().split('\n\n')]
    data = [list(map(int, value)) for value in data]

# part one
print(max(sum(calorieList) for calorieList in data))

# part two
print(sum(sorted(sum(calorieList) for calorieList in data)[-3:]))
