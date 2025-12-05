Position = tuple[int, int]
Field = list[list[str]]


def check_bounds(x: int, y: int, field: Field) -> bool:
    if x >= len(field[0]) or 0 > x:
        return False
    if y >= len(field) or 0 > y:
        return False

    return True


def get_roll_count(x: int, y: int, field: Field) -> int:
    count: int = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j
            if (i != 0 or j != 0) and check_bounds(new_x, new_y, field):
                if field[new_y][new_x] == "@":
                    count += 1

    return count


def main() -> None:
    _sum = 0

    with open('input.txt', "r") as f:
        field = [[pos for pos in line[:-1]] for line in f.readlines()]

    current = 1  # so that while loop runs

    while current > 0:
        new_field: Field = [row.copy() for row in field]
        current: int = 0

        for y, row in enumerate(field):
            for x, cell in enumerate(row):
                if cell == "@" and get_roll_count(x, y, field) < 4:
                    new_field[y][x] = "x"
                    current += 1

        _sum += current
        field = new_field

    print(_sum)


if __name__ == "__main__":
    main()
