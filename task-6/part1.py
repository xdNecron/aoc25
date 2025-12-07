with open('input.txt', "r") as f:
    lines = [line[:-1] for line in f.readlines()]

cols = []

for line in lines:
    tokens = [token for token in line.split(" ") if token != '']
    cols.append(tokens)

tasks = []
for i in range(len(cols[0])):
    task = [col[i] for col in cols]
    tasks.append(task)

_sum = 0

for task in tasks:
    _sum += eval(task.pop().join(task))

print(_sum)
