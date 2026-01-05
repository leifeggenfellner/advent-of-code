def process_part1(crates: list[list[str]], moves: str) -> str:
    moves = [[int(move.split(' ')[1]), int(move.split(' ')[3]) - 1, int(move.split(' ')[5]) - 1]
             for move in moves.splitlines()]

    for move in moves:
        for _ in range(move[0]):
            crates[move[2]].append(crates[move[1]].pop())

    return "".join(crate[-1] for crate in crates)


def process_part2(crates: list[list[str]], moves: str) -> str:
    moves = [[int(move.split(' ')[1]), int(move.split(' ')[3]) - 1, int(move.split(' ')[5]) - 1]
             for move in moves.splitlines()]

    for move in moves:
        crates_to_move = crates[move[1]][-move[0]:]
        crates[move[1]] = crates[move[1]][:-move[0]]
        crates[move[2]] += crates_to_move

    return "".join(crate[-1] for crate in crates)
