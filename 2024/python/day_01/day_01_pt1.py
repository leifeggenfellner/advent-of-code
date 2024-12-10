def part_1_solve(input_data):
    col1 = []
    col2 = []

    for row in input_data:
        nums = row.split()
        nums = [int(num) for num in nums]

        col1.append(nums[0])
        col2.append(nums[1])

    col1.sort()
    col2.sort()

    total = sum(abs(l - r) for l, r in zip(col1, col2))

    return total
