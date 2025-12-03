# noqa: D100

with open('input.txt', "r") as f:
    data = f.readlines()

_sum = 0

for bank in data:
    res = ""
    start = 0

    for _ in range(12):
        end = len(bank) - (12 - len(res))
        _max = start

        for j, bat in enumerate(bank[start:end], start):
            if bat == "9":
                _max = j
                break
            else:
                _max = _max if bank[_max] >= bat else j

        res += bank[_max]
        start = _max + 1

    _sum += int(res)

print(_sum)
