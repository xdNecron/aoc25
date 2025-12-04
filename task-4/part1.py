Position = tuple[int, int]
Field = list[list[str]]


def check_bounds(pos: Position, field: Field) -> bool:
    x, y = pos

    if x >= len(field[0]) or 0 > x:
        return False
    if y >= len(field) or 0 > y:
        return False

    return True


def get_neighbours(x: int, y: int, field: Field) -> list[Position]:
    res: list[Position] = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j
            if (i != 0 or j != 0) and check_bounds((new_x, new_y), field):
                if field[new_y][new_x] == "@":
                    res.append((x + i, y + j))

    return res


def main() -> None:
    _sum = 0

    with open('input.txt', "r") as f:
        field = [[pos for pos in line[:-1]] for line in f.readlines()]

    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == "@" and len(get_neighbours(x, y, field)) < 4:
                _sum += 1

    print(_sum)


if __name__ == "__main__":
    main()
