init = 50
count = 0
count2 = 0

with open("test2", "r") as inp:
    lines = inp.readlines()
    rotations = []

    for line in lines:
        if line[0] == "L":
            rotations.append(int(line[1:]) * -1)
        else:
            rotations.append(int(line[1:]))

for rot in rotations:
    while abs(rot) > 0:
        init += 1 if rot > 0 else -1
        init %= 100
        if init == 0:
            count += 1
        rot += 1 if rot < 0 else -1

for rot in rotations:
    if 0 < init + rot < 100:
        init = (init + rot) % 100
        continue

    d = init if rot < 0 else 100 - init
    rot = rot - d if rot < 0 else d - rot

print(count)
