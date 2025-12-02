#!/usr/bin/env python3

with open("input.txt", "r") as f:
    inputs = f.read()
    proc = [rng.split("-") for rng in inputs.split(",")]

_sum = 0

for low, high in proc:
    for i in range(int(low), int(high) + 1):
        string = str(i)
        for j in range(1, len(string) // 2 + 1):
            substr = string[0:j]
            occs = string.split(substr)
            if set(occs) == {""}:
                _sum += i
                break

print(_sum)
