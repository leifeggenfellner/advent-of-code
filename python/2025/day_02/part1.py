def part1(instructions: list[str]) -> int:
    """
    Calculate the sum of all numbers within given ranges that have matching left and right halves.
    This function processes a list of range instructions in the format "start-end" and identifies
    numbers within each range where the string representation can be split into two equal halves
    that are identical.
    Args:
        instructions (list): A list of strings representing ranges in the format "start-end",
                            where start and end are integers.
    Returns:
        int: The sum of all numbers across all ranges that satisfy the condition of having
             matching left and right halves when their string representation has an even length.
    Example:
        >>> part1(["1-100"])
        # Returns sum of numbers like 11, 22, 33, 44, 55, 66, 77, 88, 99
    Note:
        - Numbers with odd length string representations are skipped
        - Only numbers where the first half equals the second half are included in the sum
    """
    ans = 0

    for instruction in instructions:
        (start, end) = instruction.split("-")
        start, end = int(start), int(end)

        for number in range(start, end + 1):            
            number_str = str(number)
            length = len(number_str)
            
            if length % 2 != 0:
                continue

            l = number_str[0:length // 2]
            r = number_str[length // 2:]

            if l == r: 
                ans += number

    return ans