def part1(moves: list[str]) -> int:
    """
    Calculate the number of times a position reaches a multiple of 100.

    Starting from an initial position of 50, processes a series of moves where each move
    consists of a direction ('L' for left/negative, 'R' for right/positive) followed by
    a step size. Counts how many times the position lands exactly on a multiple of 100.

    Args:
        moves: A list of move strings, where each string starts with 'L' or 'R'
               followed by a numeric step size (e.g., 'L25', 'R50').

    Returns:
        The count of times the position is exactly divisible by 100 during the
        sequence of moves.

    Example:
        >>> part1(['R50', 'L25', 'R75'])
        2
    """
    initial = 50
    count = 0

    for m in moves:
        direction = -1 if m[0] == "L" else 1
        step = int(m[1:])

        initial += direction * step

        if initial % 100 == 0:
            count += 1

    return count