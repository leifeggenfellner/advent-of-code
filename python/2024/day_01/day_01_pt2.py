def part_2_solve(input_data):

    col1 = []
    col2 = []

    for row in input_data:
        nums = row.split()
        nums = [int(num) for num in nums]

        col1.append(nums[0])
        col2.append(nums[1])

    counts = {}

    total = 0

    for num in col1:
        if num in counts.keys():
            total += num * counts[num]
        else:
            count = col2.count(num)
            counts[num] = count
            total += num * count

    return total
