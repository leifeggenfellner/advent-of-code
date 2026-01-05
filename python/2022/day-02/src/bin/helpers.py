def process_part1(moves: list[str]) -> int:
    opponent_moves, player_moves = zip(
        *[line.strip().split(" ") for line in moves.splitlines()])

    equivalent_moves = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    player_wins = {'Y': 'A', 'Z': 'B', 'X': 'C'}
    move_points = {'X': 1, 'Y': 2, 'Z': 3}

    total_points = 0

    for opponent_move, player_move in zip(opponent_moves, player_moves):
        total_points += move_points[player_move]

        if opponent_move == equivalent_moves[player_move]:
            total_points += 3
        elif opponent_move == player_wins[player_move]:
            total_points += 6

    return total_points


def process_part2(moves: list[str]) -> int:
    opponent_moves, results = zip(
        *[line.strip().split(" ") for line in moves.splitlines()])

    draw = {'A': 'R', 'B': 'P', 'C': 'S'}
    player_wins = {'A': 'P', 'B': 'S', 'C': 'R'}
    player_losses = {'A': 'S', 'B': 'R', 'C': 'P'}
    move_points = {'R': 1, 'P': 2, 'S': 3}

    total_points = 0

    for opponent_move, result in zip(opponent_moves, results):
        match result:
            case 'X':
                total_points += move_points[player_losses[opponent_move]]
            case 'Y':
                total_points += 3 + move_points[draw[opponent_move]]
            case 'Z':
                total_points += 6 + move_points[player_wins[opponent_move]]

    return total_points
