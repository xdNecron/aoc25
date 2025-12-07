def get_all(plan: list[list[str]]) -> list[list[str]]:
    lines = [line.copy() for line in plan]

    for i, elem in enumerate(lines[0]):
        if elem == "S":
            lines[1][i] = "|"
            break

    for row, line in enumerate(lines[1:], 1):
        for col, elem in enumerate(line):
            if elem == "^" and lines[row - 1][col] == "|":
                line[col - 1], line[col + 1] = "|", "|"
            if elem == "." and lines[row - 1][col] == "|":
                line[col] = "|"

    return lines


def main():
    with open("input.txt", "r") as f:
        lines = [[char for char in line[:-1]] for line in f.readlines()]

    paths = {k: 0 for k in range(len(lines[0]))}
    paths[lines[0].index("S")] = 1

    count = 0
    for row, line in enumerate(lines[1:], 1):
        for col, elem in enumerate(line):
            if elem == "^" and paths[col] > 0:
                paths[col + 1] = paths.get(col + 1) + paths[col]
                paths[col - 1] = paths.get(col - 1) + paths[col]
                paths[col] = 0

    print(sum(paths.values()))


if __name__ == '__main__':
    main()
