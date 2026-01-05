def is_invalid_id(s: str) -> bool:
    """
    Check if a string is an invalid ID based on repetition pattern rules.

    A string is considered an invalid ID if it can be formed by repeating a smaller
    substring multiple times, where the substring doesn't start with '0'.

    Args:
        s (str): The string to validate as an ID.

    Returns:
        bool: True if the string is an invalid ID (can be formed by repeating a
              non-zero-starting substring), False otherwise.

    Examples:
        >>> is_invalid_id("123123")
        True
        >>> is_invalid_id("010101")
        False
        >>> is_invalid_id("abcabc")
        True
        >>> is_invalid_id("abc")
        False
    """
    n = len(s)

    for size in range(1, n // 2 + 1):
        if n % size:
            continue

        block = s[:size]
        if block[0] != "0" and s == block * (n // size):
            return True

    return False


def part2(instructions: list[str]) -> int:
    """
    Calculate the sum of all invalid IDs within the ranges specified in the instructions.

    This function processes a list of range instructions (formatted as "start-end") and
    identifies all numbers within those ranges that are invalid IDs. It returns the sum
    of all such invalid IDs.

    Args:
        instructions (list[str]): A list of range specifications, where each string
            is formatted as "start-end" (e.g., "10-20"). Both start and end values
            are inclusive.

    Returns:
        int: The sum of all numbers within the specified ranges that are considered
            invalid IDs according to the is_invalid_id() function.

    Example:
        >>> part2(["10-15", "20-25"])
        # Returns the sum of all invalid IDs in ranges 10-15 and 20-25
    """
    total = 0

    for instruction in instructions:
        start, end = map(int, instruction.split("-"))

        for n in range(start, end + 1):
            if is_invalid_id(str(n)):
                total += n

    return total
