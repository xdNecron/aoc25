Interval = tuple[int, int]


def merge(ranges: list[Interval]) -> list[Interval]:
    merged: list[Interval] = [ranges[0]]

    for r in ranges[1:]:
        a, b = r
        if a <= merged[-1][-1] + 1:
            x, y = merged.pop()
            merged.append((x, b)) if b > y else merged.append((x, y))
        else:
            merged.append(r)

    return merged


def main():
    with open('input.txt', "r") as f:
        ranges = []

        line = f.readline()
        while line != "\n":
            ranges.append(tuple([int(i) for i in line[:-1].split("-")]))
            line = f.readline()

    ranges.sort()
    merged: list[Interval] = merge(ranges)
    count = 0

    for x, y in merged:
        count += (y - x) + 1

    print(count)


if __name__ == "__main__":
    main()
