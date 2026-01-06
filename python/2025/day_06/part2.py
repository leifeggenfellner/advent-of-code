def part2(data: list[str]) -> int:
    lines = [line.rstrip() for line in data]

    operators = lines[-1]
    num_rows = lines[:-1]

    max_width = max(len(line) for line in num_rows)
    num_rows = [line.ljust(max_width) for line in num_rows]

    total = 0
    current_numbers = []
    current_op = None

    for col_idx in range(max_width - 1, -1, -1):
        col = ''.join(num_rows[row_idx][col_idx] for row_idx in range(len(num_rows)))
        operator = operators[col_idx] if col_idx < len(operators) else ' '

        if col.strip() == '' and operator == ' ':
            if current_numbers:
                if current_op == '+':
                    result = sum(current_numbers)
                else:
                    result = 1
                    for num in current_numbers:
                        result *= num
                total += result
                current_numbers = []
                current_op = None
        else:
            digit_str = ''.join(c for c in col if c.isdigit())
            if digit_str:
                current_numbers.append(int(digit_str))
            if operator in ('+', '*'):
                current_op = operator
    
    if current_numbers:
        if current_op == '+':
            result = sum(current_numbers)
        else:
            result = 1
            for num in current_numbers:
                result *= num
        total += result
    
    return total