def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merge overlapping or adjacent ranges into a list of non-overlapping ranges.
    This function takes a list of integer ranges (represented as tuples) and merges
    any ranges that overlap or are adjacent (differ by 1 or less). The resulting
    list contains the minimal set of non-overlapping ranges that cover the same
    integer values as the input.
    Args:
        ranges: A list of tuples, where each tuple contains two integers (start, end)
               representing a range. The ranges do not need to be sorted.
    Returns:
        A list of tuples representing merged ranges, sorted by their start values.
        Each tuple contains two integers (start, end) where start <= end.
    Example:
        >>> merge_ranges([(1, 3), (5, 7), (2, 4)])
        [(1, 4), (5, 7)]
        >>> merge_ranges([(1, 3), (4, 6), (7, 9)])
        [(1, 9)]
        >>> merge_ranges([(1, 2), (5, 6)])
        [(1, 2), (5, 6)]
    """
    
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    
    for start, end in ranges:
        if not merged:
            merged.append((start, end))
        else:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))
                
    return merged


def part2(ranges: list[str]) -> int:
    """
    Calculate the total count of numbers covered by merged ranges.

    This function takes a list of range strings, parses them into integer tuples,
    merges overlapping or adjacent ranges, and returns the total count of numbers
    covered by all merged ranges.

    Args:
        ranges (list[str]): A list of range strings in the format "start-end",
                           where start and end are integers.

    Returns:
        int: The total count of numbers covered by all merged ranges.

    Example:
        >>> part2(["1-3", "5-7", "2-4"])
        7  # Covers 1,2,3,4,5,6,7
    """
    parsed_ranges = [(int(l), int(r)) for l, r in (line.split("-") for line in ranges)]
    merged_ranges = merge_ranges(parsed_ranges)

    return sum(end - start + 1 for start, end in merged_ranges)
