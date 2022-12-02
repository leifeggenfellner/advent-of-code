def calculate_score(filename: str) -> int:
    with open(filename, 'r') as f:
        opponent_moves, results = zip(
            *[line.strip().split(" ") for line in f.readlines()])

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


def main():
    solution = calculate_score('./input.txt')
    print(solution)


main()
