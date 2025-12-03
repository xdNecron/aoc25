# noqa: D100

with open('input.txt', "r") as f:
    data = f.readlines()

res = 0
for bank in data:
    _max = 0
    for i, b1 in enumerate(bank[:-1]):  # -1 excludes '\n' character
        checked = set()
        for b2 in bank[i + 1:-1]:
            if b2 not in checked:
                _max = max(_max, int(b1 + b2))
                checked.add(b2)
    res += _max

print(res)
