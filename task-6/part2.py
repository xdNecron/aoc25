with open('input.txt', "r") as f:
    lines = [line[:-1] for line in f.readlines()]

rows = []
for line in lines:
    rows.append([token for token in line])

tasks = []
task = []
for i in range(len(rows[0])):
    token = "".join([row[i] for row in rows[:-1]]).strip()

    if token != "":
        task.append(token)
    elif token == "":
        tasks.append(task)
        task = []

tasks.append(task)

i = 0
for op in rows[-1]:
    if op != " ":
        tasks[i].append(op)
        i += 1

_sum = 0

for task in tasks:
    _sum += eval(task.pop().join(task))

print(_sum)
