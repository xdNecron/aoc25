with open('input.txt', "r") as f:
    ranges = []

    line = f.readline()
    while line != "\n":
        ranges.append(line[:-1])
        line = f.readline()

    to_check = [int(line[:-1]) for line in f.readlines()]

count = 0

for i in to_check:
    for r in ranges:
        rng = r.split("-")
        if int(rng[1]) >= i >= int(rng[0]):
            count += 1
            break

print(count)
