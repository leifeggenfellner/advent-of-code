with open("../inputs/day1.txt") as f:
    data = f.readlines()

col1 = []
col2 = []

for row in data:
    nums = row.split()
    nums = [int(num) for num in nums]

    col1.append(nums[0])
    col2.append(nums[1])

col1.sort()
col2.sort()

total = sum(abs(l - r) for l, r in zip(col1, col2))

print("Task 1:", total)

counts = {}

total = 0

for num in col1:
    if num in counts.keys():
        total += num * counts[num]
    else:
        count = col2.count(num)
        counts[num] = count
        total += num * count

print("Task 2:", total)
