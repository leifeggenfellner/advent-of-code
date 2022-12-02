def calculate_score(filename: str) -> int:
    with open(filename, 'r') as f:
        opponent_moves, player_moves = zip(
            *[line.strip().split(" ") for line in f.readlines()])

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


def main():
    solution = calculate_score('./input.txt')
    print(solution)


main()
