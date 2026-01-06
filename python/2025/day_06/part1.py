import math

def part1(nums: list[list[int]], operators: list[str]) -> int:
    total = 0
    
    for i, op in enumerate(operators):
        col = [row[i] for row in nums]
        col_sum = sum(col) if op == "+" else math.prod(col)
        total += col_sum
    
    return total