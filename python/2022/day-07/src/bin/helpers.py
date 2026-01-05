def create_file_system(data: str) -> dict:
    cwd = root = {}
    stack = []

    for line in data.splitlines():
        if line.startswith("$ "):
            if line[2] == "c":
                directory = line[5:]
                if directory == "/":
                    cwd = root
                    stack = []
                elif directory == "..":
                    cwd = stack.pop()
                else:
                    if directory not in cwd:
                        cwd[directory] = {}
                    stack.append(cwd)
                    cwd = cwd[directory]
        else:
            x, name = line.split()
            if x == "dir":
                if name not in cwd:
                    cwd[name] = {}
            else:
                cwd[name] = int(x)

    return root


def sum_directory(directory):
    if isinstance(directory, int):
        return (directory, 0)
    size = 0
    answer = 0

    for child in directory.values():
        child_size, child_answer = sum_directory(child)
        size += child_size
        answer += child_answer

    if size <= 100000:
        answer += size

    return (size, answer)


def process_part1(data: str) -> int:
    root = create_file_system(data)
    return sum_directory(root)[1]


def calculate_size(directory):
    if isinstance(directory, int):
        return directory
    return sum(map(calculate_size, directory.values()))


def smallest_over_threshold(directory, threshold):
    answer = float("inf")
    size = calculate_size(directory)
    if size >= threshold:
        answer = size

    for child in directory.values():
        if isinstance(child, int):
            continue
        child_answer = smallest_over_threshold(child, threshold)
        answer = min(answer, child_answer)

    return answer


def process_part2(data: str) -> int:
    root = create_file_system(data)
    threshold = calculate_size(root) - 40000000
    return smallest_over_threshold(root, threshold)
