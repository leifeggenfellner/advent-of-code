def part1(banks: list[str]) -> int:
    """
    Calculate the sum of two-digit numbers formed from the maximum digits in each bank string.

    For each bank string, this function:
    1. Finds the maximum digit in all positions except the last (tens place)
    2. Finds the maximum digit after the tens position through the end (ones place)
    3. Combines these two digits to form a two-digit number
    4. Sums all resulting two-digit numbers

    Args:
        banks (list[str]): A list of strings containing digit characters

    Returns:
        int: The sum of all two-digit numbers formed from the maximum digits
    """
    total = 0

    for bank in banks:
        ten = max(bank[:-1])
        one = max(bank[bank.index(ten) + 1:])
        total += int(ten + one)

    return total

