with open('./input.txt', 'r') as f:
    data = f.read().splitlines()
    data = [calorieList.split() for calorieList in " ".join([calorie if calorie !=
                                                             '' else '\t' for calorie in data]).split('\t')]
    data = [list(map(int, value)) for value in data]

# part one
print(max(sum(calorieList) for calorieList in data))

# part two
print(sum(sorted(sum(calorieList) for calorieList in data)[-3:]))
