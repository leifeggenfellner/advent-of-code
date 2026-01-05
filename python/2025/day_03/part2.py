def part2(banks: list[str]) -> int:
    """
    Extracts the largest possible 12-digit number from each bank string and returns their sum.
    For each bank string, this function iteratively selects the maximum digit from a
    sliding window, ensuring that enough digits remain to complete a 12-digit number.
    After each selection, the search window moves past the selected digit.
    Args:
        banks: A list of strings where each string contains digit characters.
    Returns:
        The sum of all 12-digit numbers extracted from the bank strings.
    Example:
        >>> part2(["123456789012"])
        987654321210
        The function selects digits greedily from left to right, always choosing
        the largest available digit while ensuring 12 total digits can be selected.
    """
    result = 0
    
    for bank in banks:
        digits = []
        start = 0
        remaining = 12

        while remaining:
            end = len(bank) - remaining + 1

            max_digit = max(bank[start:end])
            idx = bank.index(max_digit, start, end)

            digits.append(max_digit)
            start = idx + 1
            remaining -= 1
        
        result += int("".join(digits))
    
    return result