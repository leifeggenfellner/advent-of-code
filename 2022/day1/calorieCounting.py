with open('./input.txt', 'r') as f:
    data = f.read().splitlines()

inventory = []
tempList = []
for calorie in data:
    if calorie == "":
        inventory.append(tempList)
        tempList = []
    else:
        tempList.append(int(calorie))

print(max(sum(calorieList) for calorieList in inventory))
