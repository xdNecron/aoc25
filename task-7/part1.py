with open("input.txt", "r") as f:
    lines = [[char for char in line[:-1]] for line in f.readlines()]


count = 0

for i, elem in enumerate(lines[0]):
    if elem == "S":
        lines[1][i] = "|"
        break

for row, line in enumerate(lines[1:], 1):
    for col, elem in enumerate(line):
        if elem == "^" and lines[row - 1][col] == "|":
            count += 1
            line[col - 1], line[col + 1] = "|", "|"
        if elem == "." and lines[row - 1][col] == "|":
            line[col] = "|"

for line in lines:
    print("".join(line))

print(count)
