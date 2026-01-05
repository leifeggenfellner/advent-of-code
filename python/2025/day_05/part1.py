def in_range(value: int, range_tuple: tuple[int, int]) -> bool:
    """
    Check if a value falls within a given range (inclusive).

    Args:
        value: The integer value to check.
        range_tuple: A tuple containing the left and right bounds of the range (inclusive).

    Returns:
        bool: True if the value is within the range [left, right], False otherwise.

    Examples:
        >>> in_range(5, (1, 10))
        True
        >>> in_range(0, (1, 10))
        False
        >>> in_range(10, (1, 10))
        True
    """
    left, right = range_tuple
    return left <= value <= right

def part1(ranges: list[str], ingredients: list[str]) -> int:
    """
    Calculate the number of ingredients that fall within any of the given ranges.
    Args:
        ranges: A list of strings representing ranges in the format "left-right",
                where left and right are integers defining inclusive range boundaries.
        ingredients: A list of strings representing ingredient values that can be
                     converted to integers.
    Returns:
        The count of ingredients whose integer value falls within at least one
        of the specified ranges (inclusive on both ends).
    Example:
        >>> part1(["1-3", "5-7"], ["2", "4", "6"])
        2
    """
    parsed_ranges = [(int(l), int(r)) for l, r in (line.split("-") for line in ranges)]
    
    return sum(
        1 for ingredient in ingredients
        if any(left <= int(ingredient) <= right for left, right in parsed_ranges)
    )
