def part2(moves: list[str]) -> int:
    """
    Calculate the number of times a position reaches a multiple of 100.

    Starting from position 50, this function processes a series of moves and counts
    how many times the position lands exactly on a multiple of 100 (e.g., 0, 100, 200).

    Args:
        moves (list): A list of move strings where each string starts with 'L' (left/decrement)
                      or 'R' (right/increment) followed by the number of steps to take.
                      Example: ['L5', 'R10', 'L3']

    Returns:
        int: The count of times the position equals a multiple of 100 during the moves.

    Example:
        >>> part2(['R50', 'L100'])
        2
    """
    initial = 50
    count = 0

    for m in moves:
        direction = -1 if m[0] == "L" else 1
        step = int(m[1:])

        for _unused in range(step):
            initial += direction

            if initial % 100 == 0:
                count += 1

    return count